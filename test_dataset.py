import pytest

import pandas as pd


ALLOWED_COLUMN_NAMES = [
    # record_id
    "record_id",

    # default metadata
    "title",
    "abstract",
    "keywords",
    "authors",
    "year",
    "date",
    "doi",

    # custom variables
    "label_included",
    "label_abstract_screening",
    "duplicate_record_id",

    # special cases
    "pubmedID"
]


def get_datasets():
    """Get overview of all datasets"""
    return pd.read_csv("index.csv")["url"].to_list()


dataset_urls = get_datasets()


@pytest.mark.parametrize("url", dataset_urls)
def test_dataset(url):

    df = pd.read_csv(url)
    print(df)

    # test for empty column names
    assert (~df.columns.str.contains('^Unnamed')).any()

    # test column names
    for col in df.columns:
        assert col in ALLOWED_COLUMN_NAMES

    # each dataset should have record_id
    assert "record_id" in df.columns
