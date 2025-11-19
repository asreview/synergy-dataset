import tomllib
import pyalex
import unicodedata


def test_datasets_toml():

    with open("datasets.toml") as f:
        data = f.read()

    datasets = tomllib.loads(data)

    assert len(datasets["datasets"]) > 25


def test_dataset_keys():
    skip_checks = ["Improve"]

    with open("datasets.toml") as f:
        datasets = tomllib.loads(f.read())

    for dataset in datasets["datasets"]:
        print(dataset["key"], flush=True)
        if dataset["key"] in skip_checks:
            continue
        if dataset["key"] == "Farisogullari_2023":
            dataset["key"] = "Farisogulları_2023"
        if dataset["key"] == "Giesen_2021":
            dataset["key"] = "Bakker-Jacobs_2021"
        
        if dataset["key"] == "Aouad_2024":
            work = pyalex.Works()["https://openalex.org/W4396814222"]
        elif dataset["key"] == "Hilfiker_2017":
            work = pyalex.Works()["https://openalex.org/W2612715342"]
        else:
            work = pyalex.Works()["https://doi.org/" + dataset["publication"]["doi"]]

        surname = work["authorships"][0]["author"]["display_name"].split(" ")[-1]
        surname = surname.replace("‐", "-").replace("–", "-").replace("—", "-").replace("−", "-")
        surname = ''.join(
            c for c in unicodedata.normalize('NFD', surname) if unicodedata.category(c) != 'Mn'
        )

        openalex_key = f"{surname}_{work['publication_year']}"

        assert openalex_key in dataset["key"]
