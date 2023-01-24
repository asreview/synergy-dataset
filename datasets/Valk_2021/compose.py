import pandas as pd

df = pd.read_excel("https://osf.io/download/gmjcv/")

# adjust columns
df["DOI"] = "https://doi.org/" + df["DOI"].str.extract(r"(10.\S+)")

# rename columns
df.rename({"Included_fulltext": "label_included", "DOI": "doi"}, axis=1, inplace=True)

# export
df.to_csv("Valk_2021_raw.csv", index=False)

df_new = df[["doi", "label_included"]].copy()
df_new["openalex_id"] = None

df_new[["doi", "openalex_id", "label_included"]].to_csv(
    "Valk_2021_ids.csv", index=False
)
