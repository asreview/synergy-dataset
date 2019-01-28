import os

import pandas as pd


def load_drug_data(name):
    """Load drug datasets and their labels.

    params
    ------
    name: str
        The name of the dataset (should match with file name)
    """

    print("load drug dataset: {}".format(name))

    # create file path based on the argument name.
    fp = os.path.join(DRUG_DIR, name + ".csv")

    try:
        df = pd.read_csv(fp)
    except FileNotFoundError:
        raise ValueError("Dataset with name {} doesn't exist".format(name))

    # make texts and labels
    texts = (df['title'].fillna('') + ' ' + df['abstracts'].fillna(''))
    labels = (df["label2"] == "I").astype(int)

    print("number of positive labels: {}".format(labels.sum()))
    print("relative number of positive labels: {}".format(
        labels.sum() / labels.shape[0]))

    return texts.values, labels.values
