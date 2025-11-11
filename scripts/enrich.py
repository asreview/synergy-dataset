# python scripts/enrich.py -d Meijboom_2022 --title-search

import argparse
import ast
import copy
import logging
import os
import re
import unicodedata
import urllib.parse
from dataclasses import asdict, dataclass
from glob import glob
from pathlib import Path
from time import sleep

import pandas as pd
import pyalex
import requests
import tomli
from pyalex import Works


# Ensure we can use version 2 of OpenAlex (Walden)
def version(self, v):
    self._add_params("data-version", str(v))
    return self


Works.version = version

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

pyalex.config.email = "asreview@uu.nl"

LENS_TOKEN = os.getenv("LENS_TOKEN")

SPECIAL_TOKENS = """()[]{}'@#:;"%&`’,.?!/\\^®"""


# Dataclass to hold search results
@dataclass
class SearchedRecord:
    work: dict | None = None
    year: int | pd._libs.missing.NAType = pd.NA
    authors: str | pd._libs.missing.NAType = pd.NA
    method: str | None = None
    good_matches: int | pd._libs.missing.NAType = pd.NA
    openalex_year_diff: int | pd._libs.missing.NAType = pd.NA

    # Optional stats for stripped/smart
    title_stripped: str | pd._libs.missing.NAType = pd.NA
    title_matches_stripped: int | pd._libs.missing.NAType = pd.NA
    title_similarity_ratio_stripped: float | pd._libs.missing.NAType = pd.NA
    distance_stripped: float | pd._libs.missing.NAType = pd.NA
    abstract_check_stripped: int | pd._libs.missing.NAType = pd.NA
    authors_check_stripped: int | pd._libs.missing.NAType = pd.NA
    ranking_check_stripped: int | pd._libs.missing.NAType = pd.NA

    title_smart: str | pd._libs.missing.NAType = pd.NA
    title_matches_smart: int | pd._libs.missing.NAType = pd.NA
    title_similarity_ratio_smart: float | pd._libs.missing.NAType = pd.NA
    distance_smart: float | pd._libs.missing.NAType = pd.NA
    abstract_check_smart: int | pd._libs.missing.NAType = pd.NA
    authors_check_smart: int | pd._libs.missing.NAType = pd.NA
    ranking_check_smart: int | pd._libs.missing.NAType = pd.NA

    def to_dict(self):
        """Return everything as a flat dictionary for easy logging."""
        d = asdict(self)

        if isinstance(d.get("work"), dict) and "id" in d["work"]:
            d["openalex_id"] = d["work"]["id"]
        d.pop("work", None)
        return d


def make_searched_record(
    variant: str,
    work,
    year,
    authors,
    method: str,
    good_matches: int,
    openalex_year_diff: int,
    title,
    matches_title,
    title_similarity_ratio,
    distance,
    abstract_check,
    authors_check,
    ranking_check,
):
    fields = {
        f"title_{variant}": title,
        f"title_matches_{variant}": matches_title,
        f"title_similarity_ratio_{variant}": title_similarity_ratio,
        f"distance_{variant}": distance,
        f"abstract_check_{variant}": abstract_check,
        f"authors_check_{variant}": authors_check,
        f"ranking_check_{variant}": ranking_check,
    }

    return SearchedRecord(
        work=work,
        year=year,
        authors=authors,
        method=method,
        good_matches=good_matches,
        openalex_year_diff=openalex_year_diff,
        **fields,
    )


def safe_parse_list(x):
    # Check if x is a string that looks like a Python list
    if isinstance(x, str) and x.strip().startswith("[") and x.strip().endswith("]"):
        try:
            val = ast.literal_eval(x)
            # Only return it if casting was successful
            if isinstance(val, list):
                return val
        except Exception:
            pass
    # Otherwise, return as-is
    return x


def looks_like_initials(token):
    """
    Return True if token looks like initials:
      - has dots and only letters/dots/hyphens (e.g. 'M.-C.', 'N.-O.', 'S.B.')
      - or is a single letter optionally with dot
      - or is 1–2 uppercase letters (e.g. 'DU', 'AB')
    """
    if not token:
        return False
    token = token.strip()

    # Must contain only allowed characters
    if not re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ.\-\s]+", token):
        return False

    # If there are dots, likely initials (dashed or not)
    if "." in token:
        return True

    # Single-letter or uppercase short tokens
    if re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ]\.?", token):
        return True
    stripped = token.replace(" ", "")
    if 1 <= len(stripped) <= 2 and stripped.isupper():
        return True

    # Has hyphen but NO dots → likely a surname (e.g. 'Hadj-Alouane')
    return False


def normalize_authors(authors):
    """Return list of author strings (trimmed), handling ;, and, and comma variants.

    Heuristics:
      - If semicolons or ' and ' present -> split on them (do not touch internal commas).
      - Else split on commas, then:
          * If fragments look like alternating "Lastname" / "Given(s)" fragments (e.g. "Weinstein, G.", "Minarik, Joseph D") -> recombine pairs.
          * Otherwise treat each comma-separated fragment as its own author (covers "Heidari F.", "M Rusek", etc).
    """
    if isinstance(authors, list):
        return [a.strip() for a in authors]

    if not isinstance(authors, str):
        return []

    s = authors.strip()

    # Reliable separators first
    if re.search(r";|\band\b", s, flags=re.IGNORECASE):
        raw_parts = re.split(r";|\band\b", s, flags=re.IGNORECASE)
        parts = [p.strip() for p in raw_parts if p.strip()]
        return parts

    # No semicolons/'and' — commas might be separators or internal
    fragments = [f.strip() for f in s.split(",") if f.strip()]

    saw_bare_word = any(re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ\-']+", f) for f in fragments)

    # recombine (Lastname, Given...) pairs
    if saw_bare_word and len(fragments) >= 2:
        parts = []
        i = 0
        while i < len(fragments):
            left = fragments[i]
            right = fragments[i + 1] if i + 1 < len(fragments) else None

            left_is_bare = bool(re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ\-']+", left))
            right_is_givenish = right is not None and (
                looks_like_initials(right)
                or "." in right
                or len(right.split()) <= 2  # “Joseph D”, “A S”, etc.
            )

            if right is not None and left_is_bare and right_is_givenish:
                parts.append(f"{left}, {right}".strip())
                i += 2
            else:
                parts.append(left)
                i += 1

        return [p.strip() for p in parts if p.strip()]

    # fallback: treat all fragments as full authors
    return fragments


def extract_lastnames(authors_list):
    """Extract cleaned lastnames from a list of author strings."""
    lastnames = []
    for a in authors_list:
        if not isinstance(a, str):
            continue
        a = a.strip()

        if "," in a:
            # "lastname, given" -> take left side
            surname = a.split(",", 1)[0].strip()
        else:
            parts = a.split()
            if len(parts) == 1:
                surname = parts[0]
            else:
                last_token = parts[-1]
                if looks_like_initials(last_token):
                    # last token is initials -> surname is everything before it
                    candidate = parts[:-1]  # list of tokens
                    # strip any leading initials in candidate (e.g. "B. Hadj-Alouane" -> drop "B.")
                    while candidate and looks_like_initials(candidate[0]):
                        candidate = candidate[1:]
                    if not candidate:
                        # all tokens were initials? fallback to first token
                        surname = parts[0]
                    else:
                        surname = " ".join(candidate)
                else:
                    # last token does not look like initials -> it's the surname
                    surname = last_token

        # cleanup punctuation and stray dots
        surname = surname.replace(".", "").strip().lower()
        # skip obvious garbage or single-letter results
        if len(surname) > 1:
            lastnames.append(surname)
    return lastnames


def find_work_for_doi(doi):
    try:
        return Works()["doi:" + doi]["id"]
    except Exception as err:
        print(err)
        return None


def clean_string(s):
    s_uni = unicodedata.normalize("NFKD", s).lower()
    s_clean = "".join(i for i in s_uni if i.isalnum())
    return s_clean


def compare_titles(s1, s2, max_distance):
    s1_clean = clean_string(s1)
    s2_clean = clean_string(s2)

    return levenshtein_distance(s1_clean, s2_clean, max_distance)


# Removes all words from the title that contain a special character
def strip_title(title):
    words = title.split(" ")
    clean_words = []
    for word in words:
        if all(char.isalnum() for char in word):
            clean_words.append(word)
    clean_title = " ".join(clean_words)
    return clean_title


# Strips words from the point where they have a special character.
# Also, start by removing special characters from start.
def strip_title_smart(title):
    words = title.split(" ")
    clean_words = []
    for word in words:
        clean_chars = []
        started = False
        for char in word:
            if char.isalnum():
                started = True
                clean_chars.append(char)
            else:
                if started:
                    break
        if len(clean_chars) > 0:
            clean_words.append("".join(clean_chars))

    clean_title = " ".join(clean_words)
    return clean_title


def compare_year(y1, y2):
    return y1 == y2


def unquote_url(s):
    if not s:
        return s

    return urllib.parse.unquote(s.lower())


# Implementation based on  the "Iterative with two matrix rows" variant from wikipedia:
# https://en.wikipedia.org/wiki/Levenshtein_distance#Iterative_with_two_matrix_rows
# Some optimizations were added, based on this article:
# https://www.robertjacobson.dev/posts/2024-12-02-edit-distance-optimizations/
def levenshtein_distance(a: str, b: str, cutoff: int = 3) -> int:
    # catch some easy cases
    if a == b:
        return 0
    len_a, len_b = len(a), len(b)
    if abs(len_a - len_b) > cutoff:
        return cutoff + 1
    if len_a == 0:
        return len_b
    if len_b == 0:
        return len_a

    # ensure a is the shorter (helps memory locality)
    if len_a > len_b:
        a, b = b, a
        len_a, len_b = len_b, len_a

    previous = list(range(len_b + 1))  # full first row
    for i in range(1, len_a + 1):
        # band limits on b indices (1-based for DP columns)
        start = max(1, i - cutoff)
        end = min(len_b, i + cutoff)
        current = [cutoff + 1] * (len_b + 1)
        if start == 1:
            current[0] = i  # when j==0 is in band
        for j in range(start, end + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            sub = previous[j - 1] + cost  # substitution
            ins = current[j - 1] + 1  # insertion (into a)
            dele = previous[j] + 1  # deletion (from a)
            current[j] = min(sub, ins, dele)
        # early exit if whole band exceeds cutoff
        if min(current[start : end + 1]) > cutoff:
            return cutoff + 1
        previous = current
    res = previous[len_b]
    return res if res <= cutoff else cutoff + 1


# Does a single query on OpenAlex for 1 title.
def titlesearch_openalex(title):
    try:
        r = Works(params={"filter": {"title.search": title}}).version(2).get()
    except requests.exceptions.JSONDecodeError:
        sleep(5)
        r = Works(params={"filter": {"title.search": title}}).version(2).get()
    except requests.exceptions.RetryError:
        print("retry error for " + title)
        r = []
    return r


# Filters list of OpenAlex works based on given title
def match_title(matches, title, max_distance):
    matches_title = []
    best_match = max_distance
    for work in matches:
        if "title" in work and work["title"] and title:
            # ensure the distance is <= our best match, otherwise we stick with the better match(es)
            distance = compare_titles(work["title"], title, best_match)
            if distance < best_match:
                best_match = distance
                matches_title = [work]
            elif distance == best_match:
                matches_title.append(work)

    return matches_title, best_match


# checks if from the first 8 cleaned words of the abstract at least 6 are in the first 8 words of the OpenAlex work
def match_abstract(abstract, work):
    if "abstract_inverted_index" in work and not pd.isna(
        work["abstract_inverted_index"]
    ):
        abstract_words = abstract.split()
        words_oa = work["abstract_inverted_index"]
        if len(abstract_words) >= 8 and len(words_oa) >= 8:
            words_to_check = [clean_string(word) for word in abstract_words[:8]]
            words_base = [clean_string(word) for word in list(words_oa.keys())[:8]]
            count = 0
            for word in words_to_check:
                if word in words_base:
                    count += 1
            return count >= 6
    return False


def match_author(authors, work):
    if not (isinstance(work, dict) and "authorships" in work and work["authorships"]):
        return False

    lastnames = extract_lastnames(normalize_authors(safe_parse_list(authors)))
    if not lastnames:
        return False

    # Extract OpenAlex author surname
    oa_author = work["authorships"][0].get("author", {})
    display_name = oa_author.get("display_name", None)
    if not display_name:
        return False

    oa_surname = display_name.split()[-1].strip().lower()
    return oa_surname in lastnames


def check_record_set(title, title_to_match, abstract, authors, year, variant):
    # Initialize NA metrics
    abstract_check = authors_check = ranking_check = pd.NA

    # the maximum distance allowed for titles to match
    max_distance = min(len(title_to_match) // 20, 5)

    works = titlesearch_openalex(title)
    matches_title, distance = match_title(works, title_to_match, max_distance)

    # if no title matches: return empty
    if len(matches_title) == 0:
        return make_searched_record(
            variant=variant,
            work=None,
            year=pd.NA if pd.isna(year) else year,
            authors=pd.NA if pd.isna(authors) else authors,
            method="",
            good_matches=0,
            openalex_year_diff=pd.NA,
            title=title,
            matches_title=0,
            title_similarity_ratio=pd.NA,
            distance=pd.NA,
            abstract_check=abstract_check,
            authors_check=authors_check,
            ranking_check=ranking_check,
        )

    # if we can match a record on abstract: return that record
    if not pd.isna(abstract):
        abstract_check = 0
        for work in matches_title:
            abstract_check += 1
            if match_abstract(abstract, work):
                return make_searched_record(
                    variant=variant,
                    work=work,
                    year=pd.NA if pd.isna(year) else year,
                    authors=pd.NA if pd.isna(authors) else authors,
                    method="search_title_" + variant + "_abstract",
                    good_matches=1,
                    openalex_year_diff=abs(work.get("publication_year", pd.NA) - year) if year else pd.NA,
                    title=title,
                    matches_title=len(matches_title),
                    title_similarity_ratio=1 - (distance / max(len(title_to_match), len(work["title"]))),
                    distance=distance,
                    abstract_check=abstract_check,
                    authors_check=authors_check,
                    ranking_check=ranking_check,
                )

    # if we can match a record on authors: return that record
    if not pd.isna(authors):
        authors_check = 0
        for work in matches_title:
            authors_check += 1
            if match_author(authors, work):
                return make_searched_record(
                    variant=variant,
                    work=work,
                    year=pd.NA if pd.isna(year) else year,
                    authors=pd.NA if pd.isna(authors) else authors,
                    method="search_title_" + variant + "_authors",
                    good_matches=1,
                    openalex_year_diff=abs(work.get("publication_year", pd.NA) - year) if year else pd.NA,
                    title=title,
                    matches_title=len(matches_title),
                    title_similarity_ratio=1 - (distance / max(len(title_to_match), len(work["title"]))),
                    distance=distance,
                    abstract_check=abstract_check,
                    authors_check=authors_check,
                    ranking_check=ranking_check,
                )

    # do some filtering to ensure we very likely only have good results left
    good_matches = []
    if len(title_to_match) >= 25 and len(matches_title) <= 3:
        if not pd.isna(year):
            ranking_check = 0
            fuzzy_year_matches = []

            for work in matches_title:
                ranking_check += 1
                if (
                    "publication_year" in work
                    and work["publication_year"]
                    and abs(work["publication_year"] - year) <= 1
                ):
                    fuzzy_year_matches.append(work)

            # Prefer exact year matches if any, else keep fuzzy year matches
            exact_year_matches = [
                w for w in fuzzy_year_matches if w.get("publication_year") == year
            ]
            good_matches = (
                exact_year_matches if exact_year_matches else fuzzy_year_matches
            )
        elif len(title_to_match) >= 35:
            good_matches = matches_title

    # if we have results left, score them and return the best
    best_score = -1
    best_work = None
    for work in good_matches:
        score = work["cited_by_count"] + (
            100000
            if ("abstract_inverted_index" in work and work["abstract_inverted_index"])
            else 0
        )
        if score > best_score:
            best_score = score
            best_work = work

    return make_searched_record(
        variant=variant,
        work=best_work,
        year=pd.NA if pd.isna(year) else year,
        authors=pd.NA if pd.isna(authors) else authors,
        method="search_title_" + variant + "_ranked" if best_work else "",
        good_matches=len(good_matches) if best_work else pd.NA,
        openalex_year_diff=abs(work.get("publication_year", pd.NA) - year) if year else pd.NA,
        title=title,
        matches_title=len(matches_title),
        title_similarity_ratio=1 - (distance / max(len(title_to_match), len(work["title"]))),
        distance=distance,
        abstract_check=abstract_check,
        authors_check=authors_check,
        ranking_check=ranking_check,
    )


def search_record(title, abstract=None, authors=None, year=None):
    # stripped = words with special chars stripped away
    title_stripped = strip_title(copy.copy(title))
    stripped_rec = check_record_set(
        title_stripped, title, abstract, authors, year, "stripped"
    )
    if stripped_rec.work:
        return stripped_rec

    title_smart = strip_title_smart(copy.copy(title))
    smart_rec = check_record_set(title_smart, title, abstract, authors, year, "smart")
    # Merge smart and stripped record info
    merged_fields = {
        **{k: v for k, v in vars(stripped_rec).items() if "stripped" in k},
        **{k: v for k, v in vars(smart_rec).items() if "smart" in k},
    }
    return SearchedRecord(
        work=smart_rec.work,
        year=smart_rec.year,
        authors=smart_rec.authors,
        method=smart_rec.method,
        good_matches=smart_rec.good_matches,
        **merged_fields,
    )


def openalex_work_by_id(id_list, id_type="doi", page_length=50, sleep_duration=0):
    id_list_notnull = [i for i in id_list if i is not None]
    results = {}

    print(f"OpenAlex record lookup based on {id_type}")
    for page_start in range(0, len(id_list_notnull), page_length):
        page = id_list_notnull[page_start : page_start + page_length]

        filt = {id_type: f"{'|'.join(map(str, page))}"}
        res = Works().filter(**filt).get(per_page=page_length)
        print(f"Found {len(res)} new records.")

        for w in res:
            if id_type == "pmid":
                if "pmid" in w["ids"]:
                    results[w["ids"]["pmid"]] = w["id"]
            elif id_type == "doi":
                results[w["doi"]] = w["id"]
            else:
                raise ValueError("Id type not found.")

        sleep(sleep_duration)

    # ugly
    store = []
    for x in id_list:
        try:
            oaid = results[unquote_url(x)]
        except KeyError:
            oaid = None

        store.append(oaid)

    return list(store)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Enrich metadata", description="Lookup metadata via OpenAlex"
    )
    parser.add_argument("-d", "--dataset_name", default=None)
    parser.add_argument(
        "--title-search",
        action="store_true",
    )
    parser.add_argument(
        "--inclusions-only",
        action="store_true",
    )
    args = parser.parse_args()

    # read the config file
    with open("datasets.toml", "rb") as fp:
        config = tomli.load(fp)

    for dataset in config["datasets"]:
        if args.dataset_name and dataset["key"] != args.dataset_name:
            logging.debug(f"Skip dataset {dataset['key']}")
            continue

        if "active" in dataset and not dataset["active"]:
            print(f"Not active {dataset['key']}")
            continue

        ds_glob = Path(
            list(glob(str(Path("datasets", "*", f"{dataset['key']}_ids.csv"))))[0]
        )
        df = pd.read_csv(ds_glob)

        if "pmid" not in list(df):
            df["pmid"] = None
        if "doi" not in list(df):
            df["doi"] = None

        # OpenAlex always uses lowercase doi's and matches case specific.
        df["doi"] = df["doi"].astype("string")
        df["doi"] = df["doi"].str.lower()

        try:
            for id_type in ["pmid", "doi"]:
                if id_type not in list(df):
                    continue

                # Update works based on ID
                subset = df[id_type].notnull() & df["openalex_id"].isnull()
                if df[subset].empty:
                    continue

                oaid = openalex_work_by_id(
                    df[subset][id_type].tolist(), id_type=id_type
                )

                df["openalex_id"] = df["openalex_id"].astype("string")
                df["method"] = df["method"].astype("string")

                df.loc[subset, "openalex_id"] = oaid
                df.loc[subset, "method"] = f"id_retrieval_{id_type}"

            if args.title_search:
                try:
                    dataset_key = "_".join(ds_glob.stem.split("_")[0:-1])
                    df_raw = pd.read_csv(Path(ds_glob.parent, f"{dataset_key}_raw.csv"))
                except FileNotFoundError:
                    # no title search possible as there is no raw file
                    continue

                df_raw.rename({"Publication Year": "year"}, axis=1, inplace=True)
                if "abstract" not in list(df_raw):
                    df_raw["abstract"] = None
                if "authors" not in list(df_raw):
                    df_raw["authors"] = None

                # Search records based on title/abstract/authors/year
                total_count = len(df[df["openalex_id"].isnull()])
                print(
                    f"searching {total_count} records via title/abstract/authors/year"
                )
                searched = 0
                has_title = 0
                found = 0
                for index, row in df.iterrows():
                    if (
                        args.inclusions_only
                        and df_raw.iloc[index]["label_included"] == 0
                    ):
                        continue

                    if pd.isnull(row["openalex_id"]):
                        searched += 1
                        if pd.notnull(df_raw.iloc[index]["title"]):
                            has_title += 1
                            try:
                                year = df_raw.iloc[index]["year"]
                            except Exception:
                                year = None
                            record = search_record(
                                df_raw.iloc[index]["title"],
                                df_raw.iloc[index]["abstract"]
                                if pd.notnull(df_raw.iloc[index]["abstract"])
                                else None,
                                df_raw.iloc[index]["authors"]
                                if pd.notnull(df_raw.iloc[index]["authors"])
                                else None,
                                year,
                            )

                            if record.work:
                                found += 1

                            rec_dict = record.to_dict()
                            for key, value in rec_dict.items():
                                if key not in df.columns:
                                    df[key] = pd.NA  # add missing columns dynamically
                                df.loc[index, key] = value

                        if searched % 10 == 0:
                            print(
                                f"\rsearched: {searched}/{total_count}, has title: {has_title}, found: {found}"
                            )

        except KeyboardInterrupt as _:
            print("Stop and write results so far.")
            df.to_csv(ds_glob, index=False)

        except requests.exceptions.JSONDecodeError as err:
            df.to_csv(ds_glob, index=False)
            raise err

        finally:
            df.to_csv(ds_glob, index=False)
