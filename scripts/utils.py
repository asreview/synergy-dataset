"""This script contains functionality to simplify compose scripts for new datasets"""

import pandas as pd

# All ID's we use to search in OpenAlex
ID_SET = {"doi", "pmid", "title", "year"}

# The set of columns we want to see in the output of the compose file
OUTPUT_ID_SET = [
    "openalex_id",
    "doi",
    "pmid",
    "label_included",
    "label_abstract_included",
    "method",
]


def combine_datafiles(
    search: pd.DataFrame, ft: pd.DataFrame, ti_ab: pd.DataFrame = pd.DataFrame()
):
    """Sets labels and creates a unique combined dataframe of the records"""

    # Set labels
    if not ti_ab.empty:
        search["label_abstract_included"] = 0
        ti_ab["label_abstract_included"] = 1
        ft["label_abstract_included"] = 1

        ti_ab["label_included"] = 0

    search["label_included"] = 0
    ft["label_included"] = 1

    # Merge
    df = pd.concat([ft, ti_ab, search], ignore_index=True)

    # Add missing ID columns
    for id in ID_SET.difference(list(df)):
        df[id] = None

    # Drop duplicates
    return df.drop_duplicates(subset=ID_SET, ignore_index=True)


def write_ids_files(key: str, df: pd.DataFrame):
    """Writes _ids file and raw_ids file"""

    df.to_csv(f"{key}_raw.csv", index=False)
    df.reindex(columns=OUTPUT_ID_SET).to_csv(f"{key}_ids.csv", index=False)
