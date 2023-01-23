#
#
# python scripts/enrich.py Meijboom_2022

import pandas as pd
import requests
import argparse
from pathlib import Path

from time import sleep

from pyalex import Works


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
    args = parser.parse_args()

    df = pd.read_csv(Path("datasets", args.dataset_name, f"{args.dataset_name}_ids.csv"))

    try:

        # Update works
        lookup_table = df[df["doi"].notnull() & df["openalex_id"].isnull()]["doi"].tolist()
        ids = openalex_work_by_id(lookup_table, id_type="pmid")

        for index, row in df.iterrows():
            if pd.notnull(row["doi"]):
                try:
                    df.loc[index, "openalex_id"] = ids[row["doi"]]
                except KeyError:
                    pass

    except KeyboardInterrupt as err:
        print("Stop and write results so far.")


    df.to_csv(Path("datasets", args.dataset_name, f"{args.dataset_name}_ids.csv"), index=False)
