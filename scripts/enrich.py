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
        print("on count")
        return r[0]["doi"], r[0]["id"]
    elif len(r) > 1 and "title" in r[0] and r[0]["title"].lower() == title.lower():
        print("on title")
        return r[0]["doi"], r[0]["id"]
    elif len(r) > 1 and len(list(filter(lambda x: "relevance_score" in x and x["relevance_score"] > 5000, r))) == 1:
        print("on relevance")
        return r[0]["doi"], r[0]["id"]
    else:

        print("Multiple results", m["count"])
        return None, None


def openalex_work_by_id(id_list, id_type='doi', mailto=None):
    data = {}
    page_length = 50
    for page_start in range(0, len(id_list), page_length):
        page = id_list[page_start: page_start+page_length]

        res = Works().filter(doi=f"{'|'.join(map(str, page))}").get(per_page=page_length)

        data.update({w["doi"]: w["id"] for w in res})
        sleep(1)

    return data


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        prog = 'Enrich metadata',
        description = 'Lookup metadata via OpenAlex')

    parser.add_argument('dataset_name')
    # parser.add_argument('-c', '--count')
    # parser.add_argument('-v', '--verbose',
    #                     action='store_true')  # on/off flag

    args = parser.parse_args()


    df_raw = pd.read_csv(Path("datasets", args.dataset_name, f"{args.dataset_name}_raw.csv"))
    df = pd.read_csv(Path("datasets", args.dataset_name, f"{args.dataset_name}_ids.csv"))

    try:

        if 1:
            # Update dois
            for index, row in df.iterrows():

                if pd.isnull(row["doi"]) and pd.isnull(row["openalex_id"]) and pd.notnull(df_raw.iloc[index]["title"]):
                    doi, openalex_id = search_title(df_raw.iloc[index]["title"])
                    print("Found new work for:", doi )
                    df.loc[index, "doi"] = doi
                    df.loc[index, "openalex_id"] = openalex_id
                    sleep(1)

        if 1:
            # Update works
            lookup_table = df[df["doi"].notnull() & df["openalex_id"].isnull()]["doi"].tolist()
            ids = openalex_work_by_id(lookup_table)

            for index, row in df.iterrows():
                if pd.notnull(row["doi"]):
                    try:
                        df.loc[index, "openalex_id"] = ids[row["doi"]]
                    except KeyError:
                        pass

    except KeyboardInterrupt as err:
        print("Stop and write results so far.")


    df.to_csv(Path("datasets", args.dataset_name, f"{args.dataset_name}_ids.csv"), index=False)
