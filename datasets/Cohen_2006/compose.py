import argparse

import pandas as pd
import requests



if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="Compose Cohen data")

    parser.add_argument("subset")
    parser.add_argument("--name")

    args = parser.parse_args()

    file_location = "https://dmice.ohsu.edu/cohenaa/epc-ir-data/epc-ir.clean.tsv"

    df = pd.read_table(
        file_location,
        names=["disease", "endnoteID", "id", "abstractLabel", "articleLabel"],
    )
    df["label_included"] = (df["articleLabel"] == "I").astype(int)
    df.loc[df["disease"] == "Opiods", "disease"] = "Opioids"

    # rename columns
    df.rename({"id": "pmid"}, axis=1, inplace=True)
    df["pmid"] = "https://pubmed.ncbi.nlm.nih.gov/" + df["pmid"].astype(str)
    df["doi"] = None
    df["openalex_id"] = None

    export_fp = f"{args.name}_ids.csv" if args.name else f"Cohen_2006_{args.subset}_ids.csv"

    # save results to file
    df[df["disease"] == args.subset][
        ["pmid", "doi", "openalex_id", "label_included"]
    ].to_csv(export_fp, index=False)
