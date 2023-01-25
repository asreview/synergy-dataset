import pandas as pd

import glob, json
import argparse
import logging

import natsort

from pyalex import Work


def iterworks(df):

    files = natsort.natsorted(list(glob.glob("release/Donners_2021/works_*.json")))

    for fn in files:

        logging.info("Reading works from:", fn)
        with open(fn) as f:

            works = json.load(f)

            for work in works:

                yield work

    # return df


if __name__ == "__main__":

    # argparse.ArgumentParser()
    # argparse.
    df = pd.read_csv("release/Donners_2021/Donners_2021.csv", index_col=["openalex_id"])

    result = []
    for w in iterworks(df):
        w_oa = Work(w)

        result.append(
            {
                "title": w_oa["title"],
                "abstract": w_oa["abstract"],
                "doi": w_oa["doi"],
                "included": df.loc[w_oa["id"], "label_included"],
            }
        )

    print(pd.DataFrame(result))
