import pandas as pd
from pathlib import Path
import math

import json
import tomli

from pyalex import Works


def main(key):

    df = pd.read_csv(Path("datasets", key, f"{key}_ids.csv"))

    print("Number of records in the list (before dedup)", len(df))
    print("Number of records with openalex_id", df["openalex_id"].notnull().sum())

    result = df \
        .dropna(subset="openalex_id", axis=0) \
        .sort_values("label_included", ascending=False) \
        .drop_duplicates("openalex_id") \
        .sort_index()

    print("Number of records after deduplication", len(result))

    Path("release", key).mkdir(parents=True, exist_ok=True)
    result.to_csv(Path("release", key, f"{key}.csv"), index=False)

    x = 0
    while x < len(result):

        works = Works()[result["openalex_id"].iloc[x:x+25].tolist()]

        r = (x, min(x+25, len(result)))
        with open(Path("release", key, f"works_{r[0]}_{r[1]}.json"), "w") as f:
            json.dump(works, f)

        x += 25

if __name__ == '__main__':
    with open("datasets.toml", mode="rb") as fp:
        config = tomli.load(fp)

    for dataset in config["datasets"]:
        print(dataset["key"])

        w = Works()[dataset["publication"]["openalex"]]

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


        # if dataset["key"] != "hall_2012":
        #     main(dataset["key"])

        if dataset["key"] == "Meijboom_2022":
            main(dataset["key"])



