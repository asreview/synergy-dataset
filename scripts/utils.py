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


def rename_columns(
    df: pd.DataFrame, doi: str = "", pmid: str = "", title: str = "", year: str = ""
):
    """Creates new columns for each argument provided, copying data from the input column name"""

    if doi:
        df["doi"] = df[doi]

    if pmid:
        df["pmid"] = df[pmid]

    if title:
        df["title"] = df[title]

    if year:
        df["year"] = df[year]

    return df


def extract_doi(df: pd.DataFrame, col_in:str, pre:str = "", post:str = "", overwrite:bool = False):
    """Extracts doi with regex taking into account pre and post. Stores it in doi column with doi.org prefix."""

    regex = rf"{pre}(10\.[^{post}]*)" if post else rf"{pre}(10.\S+)"
    url_prefix = "https://doi.org/"

    if ("doi" not in list(df)) or overwrite:
        df["doi"] = url_prefix + df[col_in].str.extract(regex)[0]
    else:
        # Only overwrite rows that did not have a doi yet.
        df["doi"] = df["doi"].mask(df["doi"].isnull(), url_prefix + df[col_in].str.extract(regex)[0])

    return df


def extract_pmid(df: pd.DataFrame, col_in:str, pre:str = "", post:str = "", overwrite:bool = False):
    """Extracts pmid with regex taking into account pre and post. Stores it in pmid column with pubmed prefix."""

    regex = rf"{pre}(\d+[^{post}]*)" if post else rf"{pre}(\d+)"
    url_prefix = "https://pubmed.ncbi.nlm.nih.gov/"

    if ("pmid" not in list(df)) or overwrite:
        df["pmid"] = url_prefix + df[col_in].str.extract(regex)[0]
    else:
        # Only overwrite rows that did not have a pmid yet.
        df["pmid"] = df["pmid"].mask(df["pmid"].isnull(), url_prefix + df[col_in].str.extract(regex)[0])

    return df


def extract_year(df: pd.DataFrame, col_in:str, overwrite:bool = False):
    """Extracts the number from the input column and stores it in year column."""

    regex = r"(\d+)"

    if ("year" not in list(df)) or overwrite:
        df["year"] = df[col_in].str.extract(regex)
    elif df[col_in].dtype == "object":
        # Only overwrite rows that did not have a year yet + convert to float
        df["year"] = df["year"].mask(df["year"].isnull(), df[col_in].str.extract(regex)[0].astype(float))
    else:
        # Only overwrite rows that did not have a year yet.
        df["year"] = df["year"].mask(df["year"].isnull(), df[col_in])

    return df


def extract_title(df: pd.DataFrame, col_in:str, overwrite:bool = False):
    """Copies the title from the input column and stores it in title column."""

    if ("title" not in list(df)) or overwrite:
        df["title"] = df[col_in]
    else:
        # Only overwrite rows that did not have a title yet.
        df["title"] = df["title"].mask(df["title"].isnull(), df[col_in])

    return df


def drop_duplicates(df: pd.DataFrame):
    """Input dataframe should be sorted FT -> Ti-Ab -> search. Uses the full identifier set as key."""
    return df.drop_duplicates(subset=ID_SET, ignore_index=True)


def write_ids_files(key: str, df: pd.DataFrame):
    """Writes _ids file and raw_ids file"""

    df.to_csv(f"{key}_raw.csv", index=False)
    df.reindex(columns=OUTPUT_ID_SET).to_csv(f"{key}_ids.csv", index=False)
