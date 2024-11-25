from asreview import ASReviewData
import pandas as pd
from pathlib import Path
import numpy as np

key = "Wijnen_2024"

# Data comes from: https://zenodo.org/records/13957522
search = ASReviewData.from_file("https://zenodo.org/records/13957522/files/Initial%20search%20(outreach%20included).ris").df
search["label_included"] = 0
search["label_abstract_included"] = 0

ti_ab_exclude = ASReviewData.from_file("https://zenodo.org/records/13957522/files/Excluded%20first%20round.ris").df
ti_ab = search[~search['primary_title'].isin(ti_ab_exclude['primary_title'])].reset_index(drop=True)
ti_ab["label_included"] = 0
ti_ab["label_abstract_included"] = 1

ft = ASReviewData.from_file("https://zenodo.org/records/13957522/files/Included%20papers.ris").df
ft["label_included"] = 1
ft["label_abstract_included"] = 1

# Merge and clean up files and drop duplicates (based on ID_SET)
df = pd.concat([ft,ti_ab,search], ignore_index=True)

df["doi"] = "https://doi.org/" + df["doi"].str.extract(r"(10.\S+)")
df["year"] = df["publication_year"].str.extract(r"(\d+)")
df["title"] = df["primary_title"]

df.drop_duplicates(subset=["doi","title","year"], inplace=True, ignore_index=True)

# save results to file(s)
df.to_csv(f"{key}_raw.csv", index=False)

df["openalex_id"] = None

df[["openalex_id", "doi", "label_included", "label_abstract_included"]].to_csv(f"{key}_ids.csv", index=False)
