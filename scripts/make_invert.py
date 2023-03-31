import pandas as pd
import tomli
import argparse
import logging
from glob import glob
from pathlib import Path
import itertools
import re

cols = ["abstract", "Abstract", "Abstract Note", "abstract note"]


def invert_text(s):

    if pd.isnull(s):
        return None

    match = re.match(r"(.*?)Copyright.*", s, re.MULTILINE | re.IGNORECASE)
    if match:
        s = match.group(1)

    parts = s.strip().split(" ")

    inv = {}
    for i, p in enumerate(parts):

        if p in inv and isinstance(inv[p], int):
            inv[p] = [inv[p], i]
        elif p in inv and isinstance(inv[p], list):
            inv[p] = inv[p] + [i]
        else:
            inv[p] = i

    return inv


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="Build invert metadata", description="Invert metadata via OpenAlex"
    )
    parser.add_argument("-d", "--dataset_name", default=None)
    args = parser.parse_args()

    with open("datasets.toml", "rb") as fp:
        config = tomli.load(fp)

    for dataset in config["datasets"]:

        if args.dataset_name and dataset["key"] != args.dataset_name:
            logging.debug(f"Skip dataset {dataset['key']}")
            continue

        if "active" in dataset and not dataset["active"]:
            print(f"Not active {dataset['key']}")
            continue

        print(dataset["key"])
        try:
            fp = list(glob(str(Path("datasets", "*", f"{dataset['key']}_raw.csv"))))[0]
        except IndexError:
            continue
        df = pd.read_csv(fp)

        try:
            col_name = list(set(list(df)) & set(cols))[0]
        except IndexError:
            print("Column not found")
            continue
        inv_df = df[col_name].apply(invert_text)

        fp_out = Path(fp).parent / f"{dataset['key']}_abstract_inverted_index.csv"

        inv_df.to_json(fp_out, orient="records")
