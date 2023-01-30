import pandas as pd
from pathlib import Path
import math
import argparse
from glob import glob

import json
import tomli
import requests

from pyalex import Works
from zipfile import ZipFile, ZIP_DEFLATED

PAGE_SIZE = 50

def stats(dataset_name):

    fps = list(glob(str(Path("datasets", "*", f"{dataset_name}_ids.csv"))))[0]

    df = pd.read_csv(fps)

    print("Number of records in the list (before dedup)", len(df))
    print("Number of records with openalex_id", df["openalex_id"].notnull().sum())

    result = (
        df.dropna(subset="openalex_id", axis=0)
        .sort_values("label_included", ascending=False)
        .drop_duplicates("openalex_id")
        .sort_index()
    )

    return result.shape[0], result[result["label_included"] == 1].shape[0]


def package(dataset_name, output_folder):

    fps = list(glob(str(Path("datasets", "*", f"{dataset_name}_ids.csv"))))[0]

    df = pd.read_csv(fps)

    print("Number of records in the list (before dedup)", len(df))
    print("Number of records with openalex_id", df["openalex_id"].notnull().sum())

    result = (
        df.dropna(subset="openalex_id", axis=0)
        .sort_values("label_included", ascending=False)
        .drop_duplicates("openalex_id")
        .sort_index()
    )

    n_records = result.shape[0]
    n_records_label_included = result[result["label_included"] == 1].shape[0]

    print(n_records)
    print(n_records_label_included)

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


def render_metadata(dataset_config):
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

    n, n_included = stats(dataset["key"])
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

        if dataset["key"] == args.dataset_name:

            if 1:
                meta, works = render_metadata(dataset)

                Path("..", "odss-release", args.dataset_name).mkdir(exist_ok=True, parents=True)
                with open(Path("..", "odss-release", args.dataset_name, "metadata.json"), "w") as f:
                    json.dump(meta, f, indent=2)

                with open(Path("..", "odss-release", args.dataset_name, "metadata_works.json"), "w") as f:
                    json.dump(works, f, indent=2)

            # if 1:
            #     package(args.dataset_name,
            #         Path("..", "odss-release", args.dataset_name)
            #     )
            break
    else:
        raise ValueError(f"'{args.dataset_name}' not found.")
