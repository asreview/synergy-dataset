import tomli
from pathlib import Path
import pandas as pd

import pytest


def datasets():

    with open("datasets.toml", "rb") as fp:
        config = tomli.load(fp)

    paths = []

    for dataset in config["datasets"]:

        if "active" in dataset and not dataset["active"]:
            continue

        p = list(Path("datasets").glob(str(Path("*", f"{dataset['key']}_ids.csv"))))[0]
        paths.append(p)

    return paths

DATASETS = datasets()

@pytest.mark.parametrize("dataset", DATASETS)
def test_all_inclusions_found(dataset):

    df = pd.read_csv(dataset)
    n = df[(df["label_included"] == 1) & (df["openalex_id"].isnull())].shape[0]

    assert n == 0

@pytest.mark.parametrize("dataset", DATASETS)
def test_retrieval_rate_10(dataset):

    df = pd.read_csv(dataset)

    perc = (df["openalex_id"].isnull().sum() / len(df))*100

    assert perc < 5
