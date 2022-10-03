import pandas as pd

import requests

file_location = "https://dmice.ohsu.edu/cohenaa/epc-ir-data/epc-ir.clean.tsv"

df = pd.read_table(file_location, names=["disease", "endnoteID", "id", "abstractLabel", "articleLabel"])
df["id_type"] = "pmid"
df["label_included"] = (df["articleLabel"] == "I").astype(int)

# save results to file
for disease in df["disease"].unique():
	df[df["disease"] == disease][["id", "id_type", "label_included"]].to_csv(f"Cohen_2006_{disease}_ids.csv", index=False)


