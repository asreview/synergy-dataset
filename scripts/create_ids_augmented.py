# python scripts/create_ids_augmented.py

import pandas as pd
import numpy as np
import pyalex
from pathlib import Path
import tomli

# globals
OPENALEX_MAX_OR_LENGTH = 100
OPENALEX_MAX_PAGE_LENGTH = 200
OPENALEX_PREFIX = "https://openalex.org/"
SEED = 535


def abs_length_ok(row):
    return len(str(row["abstract"]).split()) >= 20 or len(str(row["abstract"])) >= 100


with open("datasets.toml", "rb") as fp:
    config = tomli.load(fp)

for dataset in config["datasets"]:
    print("\n============================================")
    print("Processing dataset:", dataset["key"])
    print("============================================")

    # find the corresponding CSVs
    ids_path = Path("datasets", dataset["key"], f"{dataset['key']}_ids.csv")
    raw_path = Path("datasets", dataset["key"], f"{dataset['key']}_raw.csv")
    aug_path = Path("datasets", dataset["key"], f"{dataset['key']}_ids_augmented.csv")

    # load CSVs
    df_ids = pd.read_csv(ids_path)
    df_raw = pd.read_csv(raw_path)

    # add abstract to ids file
    df_ids["abstract"] = df_raw["abstract"] if "abstract" in df_raw else ""
    df_ids["abstract_ok"] = df_ids.apply(abs_length_ok, axis=1)
    df_ids["abstract_method"] = df_ids.apply(
        lambda x: "user" if len(str(x["abstract"])) > 5 else "", axis=1
    )

    # add order
    np.random.seed(SEED)
    order_rows = np.arange(len(df_ids))
    np.random.shuffle(order_rows)
    df_ids["order"] = order_rows

    # drop na and duplicates on openalex_id
    df = (
        df_ids.sort_values(
            ["label_included", "label_abstract_included"], ascending=False
        )
        .dropna(subset="openalex_id", axis=0)
        .drop_duplicates("openalex_id")
        .sort_values("order")
    )

    # keep old doi for reference
    df["doi_original"] = df["doi"]
    df["doi"] = df["doi"].astype("string")
    df["doi_original"] = df["doi_original"].astype("string")

    # retrieve doi's from openalex
    USED_FIELDS = ["doi", "id"]
    page_length = min(OPENALEX_MAX_OR_LENGTH, OPENALEX_MAX_PAGE_LENGTH)

    for i in range(0, df.shape[0], page_length):
        fltr = "|".join(
            identifier.removeprefix(OPENALEX_PREFIX)
            for identifier in df["openalex_id"][i : i + page_length]
        )
        for work in (
            pyalex.Works()
            .filter(openalex=fltr)
            .select(USED_FIELDS)
            .get(per_page=page_length)
        ):
            if work["doi"]:
                df.loc[df["openalex_id"].str.lower() == str(work["id"]).lower(), "doi"] = work["doi"]

    # write csv
    df.to_csv(str(aug_path), index=False)
