import argparse

import numpy as np
import pandas as pd

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="Compose Yu data")
    parser.add_argument("subset")
    args = parser.parse_args()

    if args.subset == "Hall_2012":
        df = pd.read_csv("https://zenodo.org/record/1162952/files/Hall.csv")

    if args.subset == "Radjenovic_2013":
        df = pd.read_csv(
            "https://zenodo.org/record/1162952/files/Radjenovic.csv",
            encoding="iso-8859-1",
        )

    # IEEE link doesn't match record. Considered unreliable.
    # if args.subset == "Kitchenham_2010":
    #     zip_kitchenham = ZipFile(BytesIO(urlopen("https://zenodo.org/record/1162952/files/Kitchenham.zip").read()), "r")
    #     df = pd.read_csv(zip_kitchenham.open("Kitchenham/Kitchenham.csv"), encoding="iso-8859-1")

    if args.subset == "Wahono_2015":
        df = pd.read_csv(
            "https://zenodo.org/record/1162952/files/Wahono.csv"
        )  # no metadata on publication

    df.to_csv(f"{args.subset}_raw.csv", index=False)

    df["label_included"] = np.where(df["label"] == "yes", 1, 0)
    df["doi"] = None
    df["openalex_id"] = None
    df[["doi", "openalex_id", "label_included"]].to_csv(
        f"{args.subset}_ids.csv", index=False
    )
