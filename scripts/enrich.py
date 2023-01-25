#
#
# python scripts/enrich.py Meijboom_2022

import pandas as pd
import requests
import argparse
from pathlib import Path

from time import sleep

from pyalex import Works


def find_work_for_doi(doi):

    try:
        return Works()["doi:" + doi]["id"]
    except Exception as err:
        print(err)
        return None


def search_title(title):

    r, m = Works().search(title).get(return_meta=True)
    print(title)
    print("\n\n")

    if len(r) == 1:
        print("Single hit: count==1")
        return r[0]["doi"], r[0]["id"]
    elif len(r) > 1 and "title" in r[0] and r[0]["title"].lower() == title.lower():
        print("on title")
        return r[0]["doi"], r[0]["id"]
    elif (
        len(r) > 1
        and len(
            list(
                filter(
                    lambda x: "relevance_score" in x and x["relevance_score"] > 5000, r
                )
            )
        )
        == 1
    ):
        print("on relevance")
        return r[0]["doi"], r[0]["id"]
    else:

        print("Multiple results", m["count"])
        return None, None


def openalex_work_by_id(
    id_list, id_type="doi", page_length=50, sleep_duration=0.5, mailto=None
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
            else:
                results[w[id_type]] = (
                    w["doi"],
                    w["ids"]["pmid"] if "pmid" in w["ids"] else None,
                    w["id"],
                )

        sleep(sleep_duration)

    # ugly
    store = []
    for x in id_list:

        try:
            doi = results[x][0]
        except KeyError:
            if id_type == "doi":
                doi = x
            else:
                doi = None

        try:
            pmid = results[x][1]
        except KeyError:
            if id_type == "pmid":
                pmid = x
            else:
                pmid = None

        try:
            oaid = results[x][2]
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

    parser.add_argument("collection")
    parser.add_argument("-d", "--dataset_name")
    args = parser.parse_args()

    if args.dataset_name is None:
        fn = args.collection
    else:
        fn = args.dataset_name

    try:
        df_raw = pd.read_csv(Path("datasets", args.collection, f"{fn}_raw.csv"))
    except FileNotFoundError:
        pass

    df = pd.read_csv(Path("datasets", args.collection, f"{fn}_ids.csv"))

    try:

        # if 0:
        #     # Update dois
        #     for index, row in df.iterrows():

        #         if pd.isnull(row["doi"]) and pd.isnull(row["openalex_id"]) and pd.notnull(df_raw.iloc[index]["title"]):
        #             doi, openalex_id = search_title(df_raw.iloc[index]["title"])
        #             print("Found new work for:", doi )
        #             df.loc[index, "doi"] = doi
        #             df.loc[index, "openalex_id"] = openalex_id
        #             sleep(1)

        for id_type in ["pmid", "doi"]:
            # Update works based on ID
            subset = df[id_type].notnull() & df["openalex_id"].isnull()
            doi, pmid, oaid = openalex_work_by_id(
                df[subset][id_type].tolist(), id_type=id_type
            )

            df.loc[subset, "doi"] = doi
            df.loc[subset, "openalex_id"] = oaid
            if "pmid" in list(df):
                df.loc[subset, "pmid"] = pmid

    except KeyboardInterrupt as err:
        print("Stop and write results so far.")

    df.to_csv(Path("datasets", args.collection, f"{fn}_ids.csv"), index=False)
