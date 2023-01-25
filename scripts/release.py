import pandas as pd
from pathlib import Path
import math
import argparse

import json
import tomli

from pyalex import Works
from zipfile import ZipFile, ZIP_DEFLATED

PAGE_SIZE = 50


def main(key):

    df = pd.read_csv(Path("datasets", key, f"{key}_ids.csv"))

    print("Number of records in the list (before dedup)", len(df))
    print("Number of records with openalex_id", df["openalex_id"].notnull().sum())

    result = (
        df.dropna(subset="openalex_id", axis=0)
        .sort_values("label_included", ascending=False)
        .drop_duplicates("openalex_id")
        .sort_index()
    )

    print("Number of records after deduplication", len(result))

    Path("..", "odss-release", key).mkdir(parents=True, exist_ok=True)
    result.to_csv(Path("..", "odss-release", key, f"{key}.csv"), index=False)

    # create zip
    with ZipFile(
        Path("..", "odss-release", key, f"works.zip"), "w", ZIP_DEFLATED
    ) as zip_obj:

        x = 0
        while x < len(result):

            works = Works()[result["openalex_id"].iloc[x : x + PAGE_SIZE].tolist()]

            r = (x, min(x + PAGE_SIZE, len(result)))

            zip_obj.writestr(f"works_{r[0]}_{r[1]}.json", json.dumps(works))

            # with open(Path("..", "odss-release", key, f"works_{r[0]}_{r[1]}.json"), "w") as f:
            #     json.dump(works, f)

            x += PAGE_SIZE


def render_metadata(config):

    for dataset in config["datasets"]:
        print(dataset["key"])

        w = Works()["doi:" + dataset["publication"]["doi"]]

        print(w["doi"])
        print(w["title"])
        # print(w["authorships"])
        print([x["author"]["display_name"] for x in w["authorships"]])
        print(w["host_venue"]["display_name"])
        print(w["publication_year"])

        # "Hall_2012": {
        #   "link": "http://doi.org/10.5281/zenodo.1162952",
        #   "license": "CC-BY Attribution 4.0 International",

        #   "topic": "Software Fault Prediction",
        #   "final_inclusions": true,
        #   "title_abstract_inclusions": false,
        # },

    return


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="Build release metadata", description="Lookup metadata via OpenAlex"
    )

    parser.add_argument("dataset_name")
    args = parser.parse_args()

    with open("datasets.toml", mode="rb") as fp:
        config = tomli.load(fp)

    # render_metadata()

    for dataset in config["datasets"]:

        if dataset["key"] == args.dataset_name:
            main(args.dataset_name)
