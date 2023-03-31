import pandas as pd
from pathlib import Path
import math
import argparse
import logging
from glob import glob

import json
import tomli
import requests
import numpy as np

import pyalex
from pyalex import Works
from zipfile import ZipFile, ZIP_DEFLATED

PAGE_SIZE = 25
pyalex.config.email = "asreview@uu.nl"

SEED = 535


def stats(labels_path):

    df = pd.read_csv(labels_path)

    return df.shape[0], df[df["label_included"] == 1].shape[0]


def package(dataset_name, output_folder):

    fps = list(glob(str(Path("datasets", "*", f"{dataset_name}_ids.csv"))))[0]

    df = pd.read_csv(fps)

    print("Number of records in the list", len(df))
    print("Number of records with openalex_id", df["openalex_id"].notnull().sum())

    print("Number of included records with openalex_id", df["label_included"].sum())

    # add order
    np.random.seed(SEED)
    order_rows = np.arange(len(df))
    np.random.shuffle(order_rows)
    df["order"] = order_rows

    result = (
        df.sort_values("label_included", ascending=False)
        .dropna(subset="openalex_id", axis=0)
        .drop_duplicates("openalex_id")
        .sort_values("order")
    )

    # some datasets don't have pmid (like hall)
    if "pmid" not in list(df):
        result["pmid"] = None

    result = result[["openalex_id", "doi", "pmid", "label_included"]]

    if len(result) == 0:
        raise ValueError("No records in dataset after deduplication. Check dataset.")

    print("Number of records after deduplication", len(result))

    Path(output_folder).mkdir(parents=True, exist_ok=True)
    result.to_csv(Path(output_folder, "labels.csv"), index=False)

    # create zip
    with ZipFile(Path(output_folder, f"works.zip"), "w", ZIP_DEFLATED) as zip_obj:

        x = 0
        while x < len(result):

            works = Works()[result["openalex_id"].iloc[x : x + PAGE_SIZE].tolist()]

            r = (x, min(x + PAGE_SIZE, len(result)))

            zip_obj.writestr(f"works_{r[0]}_{r[1]}.json", json.dumps(works))

            x += PAGE_SIZE


def render_metadata(dataset_config, labels_path):
    # Add license info?

    config = dataset_config.copy()

    try:
        del config["scripts"]
    except KeyError:
        pass

    try:
        print("Metadata of", dataset["key"])

        w = Works()["doi:" + dataset["publication"]["doi"]]

    except requests.exceptions.HTTPError as err:
        print("ERROR with metadata of {}:".format(dataset["key"]), err)

    # get the APA style citation
    r = requests.get(
        "https://doi.org/" + dataset["publication"]["doi"],
        headers={"accept": "text/x-bibliography; style=apa; charset=utf-8"}
    )
    r.encoding = "utf-8"
    dataset["publication"]["citation"] = {"apa": r.text}

    # add stats
    n, n_included = stats(labels_path)
    config["data"]["n_records"] = n
    config["data"]["n_records_included"] = n_included

    return config, dict(w)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="Build release metadata", description="Lookup metadata via OpenAlex"
    )

    parser.add_argument("-d", "--dataset_name", default=None)
    # parser.add_argument("--meta")
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

        output_path = Path("..", "synergy-release", dataset["key"])
        output_path.mkdir(exist_ok=True, parents=True)

        if 1:
            package(args.dataset_name, output_path)

        if 1:
            meta, works = render_metadata(dataset, Path(output_path, "labels.csv"))

            with open(Path(output_path, "metadata.json"), "w") as f:
                json.dump(meta, f, indent=2)

            with open(Path(output_path, "publication_metadata.json"), "w") as f:
                json.dump(works, f, indent=2)
