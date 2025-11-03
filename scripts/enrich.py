# python scripts/enrich.py -d Meijboom_2022 --title-search

import os
import copy
import pandas as pd
import requests
import argparse
from pathlib import Path
from glob import glob
import unicodedata
import urllib.parse
import tomli


from time import sleep

import pyalex
from pyalex import Works


# Ensure we can use version 2 of OpenAlex (Walden)
def version(self, v):
    self._add_params("data-version", str(v))
    return self


Works.version = version

import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


pyalex.config.email = "asreview@uu.nl"

LENS_TOKEN = os.getenv("LENS_TOKEN")

SPECIAL_TOKENS = """()[]{}'@#:;"%&`’,.?!/\\^®"""


def find_work_for_doi(doi):
    try:
        return Works()["doi:" + doi]["id"]
    except Exception as err:
        print(err)
        return None


def compare_titles(s1, s2, max_distance):
    # print(compare_titles("Test & orčpžsíáýd", "Testorcpzsiayd"))

    s1_uni = unicodedata.normalize("NFKD", s1).lower()
    s2_uni = unicodedata.normalize("NFKD", s2).lower()

    s1_clean = "".join(i for i in s1_uni if i.isalnum())
    s2_clean = "".join(i for i in s2_uni if i.isalnum())

    return Levenshtein_distance(s1_clean, s2_clean, max_distance)


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
def strip_title_from_special(title):
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


# Filters list of OpenAlex works based on given year
def match_year(matches, year):
    matches_year = []
    for work in matches:
        if (
            "publication_year" in work
            and work["publication_year"]
            and year
            and work["publication_year"] == year
        ):
            matches_year.append(work)

    return matches_year


def search_record(title, year=None, label_included=None):
    # the maximum distance allowed for titles to match
    max_distance = min(len(title) // 20, 5)

    title_raw = copy.copy(title)

    # stripped = words with special chars stripped away
    title_stripped = strip_title(copy.copy(title))
    works = titlesearch_openalex(title_stripped)

    matches_title, distance = match_title(works, title, max_distance)
    if len(matches_title) == 1:
        return matches_title[0], "search_title", len(matches_title), distance

    matches_year = match_year(matches_title, year)
    if len(matches_year) == 1:
        return matches_year[0], "search_title_year", len(matches_year), distance

    # If stripped title has < 5 words, do a different search as well.
    if len(title_stripped.split(" ")) < 5:
        title_smart = strip_title_from_special(copy.copy(title))
        works = titlesearch_openalex(title_smart)

        matches_title_smart, distance = match_title(works, title, max_distance)
        if len(matches_title_smart) == 1:
            return (
                matches_title_smart[0],
                "search_title_extra",
                len(matches_title_smart),
                distance,
            )

        matches_year = match_year(matches_title_smart, year)
        if len(matches_year) == 1:
            return (
                matches_year[0],
                "search_title_year_extra",
                len(matches_title_smart),
                distance,
            )

    # added str(len(matches_title)) for now, because the next step is to look at cases with 2+ records.
    return None, None, str(len(matches_title)), distance


def openalex_work_by_id(
    id_list, id_type="doi", page_length=50, sleep_duration=0, mailto=None
):
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

        # add the collection method
        if "method" not in list(df):
            df["method"] = None
        if "matches" not in list(df):
            df["matches"] = None
        if "distance" not in list(df):
            df["distance"] = None
        if "oa_title" not in list(df):
            df["oa_title"] = None

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

                # Update dois from title
                total_count = len(df[df["openalex_id"].isnull()])
                print(f"searching {total_count} records via title/year")
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
                            record, retrieval_method, matches, distance = search_record(
                                df_raw.iloc[index]["title"],
                                year,
                                df_raw.iloc[index]["label_included"],
                            )

                            if record:
                                found += 1
                                df.loc[index, "openalex_id"] = record["id"]
                                df.loc[index, "oa_title"] = record["title"]
                            df.loc[index, "method"] = retrieval_method
                            df.loc[index, "matches"] = matches
                            df.loc[index, "distance"] = distance

                        if searched % 10 == 0:
                            print(
                                f"\rsearched: {searched}/{total_count}, has title: {has_title}, found: {found}"
                            )

        except KeyboardInterrupt as err:
            print("Stop and write results so far.")
            df.to_csv(ds_glob, index=False)

        except requests.exceptions.JSONDecodeError as err:
            df.to_csv(ds_glob, index=False)
            raise err

        finally:
            df.to_csv(ds_glob, index=False)
