from synergy_dataset import Dataset, iter_datasets

import pytest


@pytest.mark.parametrize("dataset", iter_datasets())
def test_abstract_included_missing(dataset):

    df = dataset.to_frame()
    print(dataset.name)

    assert df.loc[df["label_included"] == 1, "abstract"].isnull().sum() == 0
