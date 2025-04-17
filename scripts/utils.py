"""This script contains functionality to simplify compose scripts for new datasets"""

import pandas as pd
from pandas.api.types import is_string_dtype
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
import os
import urllib.parse

# All ID's we use to search in OpenAlex
ID_SET = {"openalex_id","doi", "pmid", "title", "year"}

# The set of columns we want to see in the output of the compose file
OUTPUT_ID_SET = [
    "openalex_id",
    "doi",
    "pmid",
    "label_included",
    "label_abstract_included",
    "method",
]


def unquote_nan(x):
    try:
        return urllib.parse.unquote(x)
    except Exception:
        return None


def unzip(zip_path, filename="", new_filename=""):
    """Unzips a zip, stored either locally or online. Can target a specific file and possible rename it."""

    # Load zip file, either local or online
    if os.path.isfile(zip_path):
        zip_file = ZipFile(zip_path, "r")
    else:
        resp = urlopen(zip_path)
        zip_file = ZipFile(BytesIO(resp.read()))

    # Do the extraction
    if filename:
        if not os.path.isfile(filename):
            zip_file.extract(filename)
    else:
        zip_file.extractall()

    zip_file.close()

    # Rename
    if new_filename and not os.path.isfile(new_filename):
        os.rename(filename, new_filename)


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
    df = df.reindex(columns=list(df) + list(ID_SET.difference(list(df))))

    return df


def rename_columns(
    df: pd.DataFrame,
    doi: str = "",
    pmid: str = "",
    title: str = "",
    year: str = "",
    ft_label: str = "",
    ti_ab_label: str = "",
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

    if ft_label:
        df["label_included"] = df[ft_label]

    if ti_ab_label:
        df["label_abstract_included"] = df[ti_ab_label]

    return df


def extract_doi(
    df: pd.DataFrame,
    col_in: str,
    pre: str = "",
    post: str = "",
    overwrite: bool = False,
    unquote: bool = True,
):
    """Extracts doi with regex taking into account pre and post. Stores it in doi column with doi.org prefix."""

    # Sometimes the column is a list, we need it to be a string
    df[col_in] = df[col_in].astype("string")

    regex = rf"{pre}(10\.[^{post}]*)" if post else rf"{pre}(10\.\S+)"
    url_prefix = "https://doi.org/"

    if ("doi" not in list(df)) or overwrite:
        df["doi"] = url_prefix + df[col_in].str.extract(regex)[0]
    else:
        # Only overwrite rows that did not have a doi yet.
        df["doi"] = df["doi"].mask(
            df["doi"].isnull(), url_prefix + df[col_in].str.extract(regex)[0]
        )

    if unquote:
        df["doi"] = df["doi"].apply(unquote_nan)

    return df


def extract_pmid(
    df: pd.DataFrame,
    col_in: str,
    pre: str = "",
    overwrite: bool = False,
    numbers_only: bool = False,
):
    """Extracts pmid with regex taking into account pre and post. Stores it in pmid column with pubmed prefix."""

    # Optinally get rid of any input value that is not a number
    if numbers_only:
        mask = df[col_in].notnull() & df[col_in].str.isdigit()
        df.loc[mask, "new_col_in"] = df.loc[mask, col_in]
        df[col_in] = df["new_col_in"]

    # In case only numbers exist in the column, convert it to string
    df[col_in] = df[col_in].astype("string")

    regex = rf"{pre}(\d+)"
    url_prefix = "https://pubmed.ncbi.nlm.nih.gov/"

    if ("pmid" not in list(df)) or overwrite:
        df["pmid"] = url_prefix + df[col_in].str.extract(regex)[0]
    else:
        # Only overwrite rows that did not have a pmid yet.
        df["pmid"] = df["pmid"].mask(
            df["pmid"].isnull(), url_prefix + df[col_in].str.extract(regex)[0]
        )

    return df


def extract_year(df: pd.DataFrame, col_in: str, overwrite: bool = False):
    """Extracts the number from the input column and stores it in year column."""

    regex = r"(\d+)"

    if ("year" not in list(df)) or overwrite:
        df["year"] = df[col_in].str.extract(regex)
    elif is_string_dtype(df[col_in].dtype):
        # Only overwrite rows that did not have a year yet + convert to float
        df["year"] = df["year"].mask(
            df["year"].isnull(), df[col_in].str.extract(regex)[0].astype(float)
        )
    else:
        # Only overwrite rows that did not have a year yet.
        df["year"] = df["year"].mask(df["year"].isnull(), df[col_in])

    return df


def extract_title(df: pd.DataFrame, col_in: str, overwrite: bool = False):
    """Copies the title from the input column and stores it in title column."""

    if ("title" not in list(df)) or overwrite:
        df["title"] = df[col_in]
    else:
        # Only overwrite rows that did not have a title yet.
        df["title"] = df["title"].mask(df["title"].isnull(), df[col_in])

    return df


def extract_labels(
    df: pd.DataFrame,
    ft_col: str,
    ft_value: str,
    ti_ab_col: str = None,
    ti_ab_value: str = "",
):
    """Create the label columns by converting given values to 1 of input columns."""

    df["label_included"] = (df[ft_col] == ft_value).astype(int)
    if ti_ab_col is not None:
        df["label_abstract_included"] = (df[ti_ab_col] == ti_ab_value).astype(int)

    return df


def drop_duplicates(df: pd.DataFrame):
    """Input dataframe should be sorted FT -> Ti-Ab -> search. Uses the full identifier set as key."""

    df = df.reindex(columns=list(df) + list(ID_SET.difference(list(df))))

    return df.drop_duplicates(subset=ID_SET, ignore_index=True)


def write_ids_files(key: str, df: pd.DataFrame):
    """Writes _ids file and raw_ids file"""

    df.to_csv(f"{key}_raw.csv", index=False)
    df.reindex(columns=OUTPUT_ID_SET).to_csv(f"{key}_ids.csv", index=False)
