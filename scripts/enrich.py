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


def compare_year(y1, y2):

    return y1 == y2


def unquote_url(s):

    if not s:
        return s

    return urllib.parse.unquote(s.lower())


def search_record(title, year=None, label_included=None):

    title_raw = copy.copy(title)

    # clean title to prevent zero hits in openalex due to bad special char
    # handling.
    for x in SPECIAL_TOKENS:
        title = title.replace(x, "")

    # search for the work on OpenAlex
    try:
        r = Works().search(title).get()
    except requests.exceptions.JSONDecodeError:
        sleep(5)
        r = Works().search(title).get()

    matches = []
    for work in r:
        if (
            "title" in work
            and work["title"]
            and title
            and compare_titles(work["title"], title)
        ):
            matches.append(work)

    # print(f"N={len(matches)}:", title)
    if len(matches) == 1:
        return matches[0]["doi"], matches[0]["id"], "search_title"

    # if there was no match of more than one match, go to this step.
    # we match year as well.
    matches_year = []
    for work in matches:
        if (
            "publication_year" in work
            and work["publication_year"]
            and year
            and work["publication_year"] == year
        ):
            matches_year.append(work)

    if len(matches_year) == 1:
        return matches_year[0]["doi"], matches_year[0]["id"], "search_title_year"

    if LENS_TOKEN and label_included == 1:
        print("Search with Lens")

        title_quote = urllib.parse.quote(title)
        url = f"https://api.lens.org/scholarly/search?query=title:({title_quote})&include=external_ids,title,year_published,lens_id&size=1&token={LENS_TOKEN}"

        r = requests.get(url)
        rdata = r.json()
        print(title)
        print(rdata)
        try:
            sleep(6)
            ids = rdata["data"][0]["external_ids"]
            doi = filter(lambda x: x["type"] == "doi", ids).__next__()["value"]
            print(doi)
            openalex_id = Works()["doi:" + doi]["id"]
            print(openalex_id)
            return None, openalex_id, "lens_lookup"
        except Exception as err:
            print(err)

    return None, None, None


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
                    results[w["ids"]["pmid"]] = (w["doi"], w["ids"]["pmid"], w["id"])
            elif id_type == "doi":
                results[w["doi"]] = (
                    w["doi"],
                    w["ids"]["pmid"] if "pmid" in w["ids"] else None,
                    w["id"],
                )
            else:
                raise ValueError("Id type not found.")

        sleep(sleep_duration)

    # ugly
    store = []
    for x in id_list:

        try:
            doi = results[unquote_url(x)][0]

        except KeyError:
            if id_type == "doi":
                doi = x
            else:
                doi = None

        try:
            pmid = results[unquote_url(x)][1]
        except KeyError:
            if id_type == "pmid":
                pmid = x
            else:
                pmid = None

        try:
            oaid = results[unquote_url(x)][2]
        except KeyError:
            oaid = None

        store.append((doi, pmid, oaid))

    return (
        list(map(lambda x: x[0], store)),
        list(map(lambda x: x[1], store)),
        list(map(lambda x: x[2], store)),
    )


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

        try:

            for id_type in ["pmid", "doi"]:

                if id_type not in list(df):
                    continue

                # Update works based on ID
                subset = df[id_type].notnull() & df["openalex_id"].isnull()
                if df[subset].empty:
                    continue

                doi, pmid, oaid = openalex_work_by_id(
                    df[subset][id_type].tolist(), id_type=id_type
                )

                # If the search did not find a doi, keep it from the input data
                if id_type != "doi":
                    dois = df[subset]["doi"].tolist()
                    for i, d in enumerate(doi):
                        if d == None:
                            doi[i] = dois[i]

                df.loc[subset, "openalex_id"] = oaid
                df.loc[subset, "doi"] = doi
                df.loc[subset, "pmid"] = pmid
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
                for index, row in df.iterrows():

                    if (
                        args.inclusions_only
                        and df_raw.iloc[index]["label_included"] == 0
                    ):
                        continue

                    if pd.isnull(row["openalex_id"]) and pd.notnull(
                        df_raw.iloc[index]["title"]
                    ):
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
                            print("Found new work:", doi)
                            df.loc[index, "openalex_id"] = openalex_id
                            df.loc[index, "method"] = retrieval_method

                        if doi:
                            df.loc[index, "doi"] = doi

        except KeyboardInterrupt as err:
            print("Stop and write results so far.")
            df.to_csv(ds_glob, index=False)

        except requests.exceptions.JSONDecodeError as err:
            df.to_csv(ds_glob, index=False)
            raise err

        finally:
            df.to_csv(ds_glob, index=False)
