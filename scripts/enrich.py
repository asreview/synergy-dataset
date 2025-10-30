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


def compare_titles(s1, s2):

    # print(compare_titles("Test & orčpžsíáýd", "Testorcpzsiayd"))

    s1_uni = unicodedata.normalize("NFKD", s1).lower()
    s2_uni = unicodedata.normalize("NFKD", s2).lower()

    s1_clean = "".join(i for i in s1_uni if i.isalnum())
    s2_clean = "".join(i for i in s2_uni if i.isalnum())

    return s1_clean == s2_clean


# Removes all words from the title that contain a special character
def strip_title(title):
    words = title.split(" ")
    clean_words = []
    for word in words:
        if all(char.isalnum() for char in word):
            clean_words.append(word)
    clean_title =  ' '.join(clean_words)
    return clean_title

# Strips words untill they reach a special character. 
# Also, start by removing special characters from start.
def strip_title_till_special(title):
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
            clean_words.append(''.join(clean_chars))

    clean_title =  ' '.join(clean_words)
    return clean_title


def compare_year(y1, y2):

    return y1 == y2


def unquote_url(s):

    if not s:
        return s

    return urllib.parse.unquote(s.lower())


# Does a single query on OpenAlex for 1 title.
def titlesearch_openalex(title):
    try:
        r = Works(params={"filter": {"title.search": title}}).version(2).get()
    except requests.exceptions.JSONDecodeError:
        r = []
    except requests.exceptions.RetryError:
        r = []
    return r


# Filters list of OpenAlex works based on given title
def match_title(matches, title):
    matches_title = []
    for work in matches:
        if (
            "title" in work
            and work["title"]
            and title
            and compare_titles(work["title"], title)
        ):
            matches_title.append(work)
    return matches_title


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

    title_raw = copy.copy(title)

    # stripped = words with special chars stripped away
    title_stripped = strip_title(copy.copy(title))

    # smart = words start at first normal character untill a special character
    title_smart = strip_title_till_special(copy.copy(title))

    # Combine title_smart with title_stripped if title_stripped >= 3.
    if len(title_stripped.split(" ")) < 3:
        title_stripped = ""
    title_combined = title_stripped + "|" + title_smart

    works = titlesearch_openalex(title_combined)

    matches_title = match_title(works, title)
    if len(matches_title) == 1:
        return matches_title[0]["doi"], matches_title[0]["id"], "search_title"

    matches_year = match_year(matches_title, year)
    if len(matches_year) == 1:
        return matches_year[0]["doi"], matches_year[0]["id"], "search_title_year"

    return None, None, str(len(matches_title))


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

        # OpenAlex always uses lowercase doi's and matches case specific.
        df['doi'] = df['doi'].astype("string")
        df["doi"] = df['doi'].str.lower()
        
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
                            doi, openalex_id, retrieval_method = search_record(
                                df_raw.iloc[index]["title"],
                                year,
                                df_raw.iloc[index]["label_included"],
                            )

                            if openalex_id:
                                found += 1
                                df.loc[index, "openalex_id"] = openalex_id
                            df.loc[index, "method"] = retrieval_method
                                
                        if searched % 10 == 0:
                            print(f"\rsearched: {searched}/{total_count}, has title: {has_title}, found: {found}")

        except KeyboardInterrupt as err:
            print("Stop and write results so far.")
            df.to_csv(ds_glob, index=False)

        except requests.exceptions.JSONDecodeError as err:
            df.to_csv(ds_glob, index=False)
            raise err

        finally:
            df.to_csv(ds_glob, index=False)
