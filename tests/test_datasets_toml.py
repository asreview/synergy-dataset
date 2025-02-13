import tomllib


def test_datasets_toml():

    with open("datasets.toml") as f:
        data = f.read()

    datasets = tomllib.loads(data)

    assert len(datasets["datasets"]) > 25
