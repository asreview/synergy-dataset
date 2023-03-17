#
#
# python scripts/enrich.py Meijboom_2022 --title-search

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

pyalex.config.email = "asreview@uu.nl"

SPECIAL_TOKENS = """()[]{}'@#:;"%&’,.?!/\\^"""


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


def search_title(title):

    # clean title to prevent zero hits in openalex due to bad special char
    # handling.
    for x in SPECIAL_TOKENS:
        title = title.replace(x, "")

    try:
        r, m = Works().search(title).get(return_meta=True)
    except requests.exceptions.JSONDecodeError:
        sleep(5)
        r, m = Works().search(title).get(return_meta=True)

    matches = []
    for work in r:
        if "title" in work and work["title"] and title and compare_titles(work["title"], title):
            matches.append(work)

    print(f"N={len(matches)}:",title)
    if len(matches) == 1:
        return matches[0]["doi"], matches[0]["id"]

    # if len(r) == 1:
    #     print("Single hit: count==1")
    #     return r[0]["doi"], r[0]["id"]
    # elif len(r) > 1 and "title" in r[0] and compare_titles(r[0]["title"], title):
    #     print("on title")
    #     return r[0]["doi"], r[0]["id"]
    # elif (
    #     len(r) > 1
    #     and len(
    #         list(
    #             filter(
    #                 lambda x: "relevance_score" in x and x["relevance_score"] > 5000, r
    #             )
    #         )
    #     )
    #     == 1
    # ):
    #     print("on relevance")
    #     return r[0]["doi"], r[0]["id"]
    # else:

    return None, None


def openalex_work_by_id(
    id_list, id_type="doi", page_length=50, sleep_duration=0, mailto=None
):

    id_list_notnull = [i for i in id_list if i is not None]
    results = {}

    print("Record lookup by ID")
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
    parser.add_argument(
        "dataset_name",
        nargs="*"
    )
    parser.add_argument(
        "--title-search", action="store_true",
    )
    args = parser.parse_args()

    # read the config file
    with open("datasets.toml", "rb") as fp:
        config = tomli.load(fp)

    for dataset in config["datasets"]:

        if dataset["key"] in args.dataset_name:

            ds_glob = Path(list(glob(str(Path("datasets", "*", f"{dataset['key']}_ids.csv"))))[0])
            df = pd.read_csv(ds_glob)

            if "pmid" not in list(df):
                df["pmid"] = None
            if "doi" not in list(df):
                df["doi"] = None

            try:

                for id_type in ["pmid", "doi"]:

                    if id_type not in list(df):
                        continue

                    # Update works based on ID
                    subset = df[id_type].notnull() & df["openalex_id"].isnull()
                    doi, pmid, oaid = openalex_work_by_id(
                        df[subset][id_type].tolist(), id_type=id_type
                    )

                    df.loc[subset, "doi"] = doi
                    df.loc[subset, "openalex_id"] = oaid
                    df.loc[subset, "pmid"] = pmid

                    # add the collection method
                    if "method" not in list(df):
                        df["method"] = None
                    df.loc[subset, "method"] = [f"id_retrieval_{id_type}" if x else None for x in oaid]

                if args.title_search:

                    try:
                        dataset_key = "_".join(ds_glob.stem.split("_")[0:-1])
                        df_raw = pd.read_csv(Path(ds_glob.parent, f"{dataset_key}_raw.csv"))
                    except FileNotFoundError:
                        # no title search possible as there is no raw file
                        continue

                    # Update dois from title
                    for index, row in df.iterrows():

                        if pd.isnull(row["openalex_id"]) and pd.notnull(df_raw.iloc[index]["title"]):
                            doi, openalex_id = search_title(df_raw.iloc[index]["title"])

                            if openalex_id:
                                print("Found new work for:", doi)
                                df.loc[index, "openalex_id"] = openalex_id
                            if doi:
                                df.loc[index, "doi"] = doi
                            if openalex_id:
                                df.loc[index, "method"] = "search_title"

            except KeyboardInterrupt as err:
                print("Stop and write results so far.")
                df.to_csv(ds_glob, index=False)

            except requests.exceptions.JSONDecodeError as err:
                df.to_csv(ds_glob, index=False)
                raise err

            finally:
                df.to_csv(ds_glob, index=False)
