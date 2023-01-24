import pandas as pd

key = "Smid_2020"

df = pd.read_csv("https://osf.io/download/gxams/", usecols=["doi", "included"])

# adjust columns
df["doi"] = "https://doi.org/" + df["doi"].str.extract(r"(10.\S+)")

# rename columns
df.rename({"included": "label_included"}, axis=1, inplace=True)

# export
df.to_csv(f"{key}_raw.csv", index=False)

df_new = df[["doi", "label_included"]].copy()
df_new["openalex_id"] = None

df_new[["doi", "openalex_id", "label_included"]].to_csv(f"{key}_ids.csv", index=False)
