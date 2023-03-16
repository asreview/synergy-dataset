import pandas as pd

key = "Jeyaraman_2020"

df = pd.read_csv("https://osf.io/download/pkc3g/", sep="\t", encoding="windows-1252", engine="python")

# rename columns
df.rename({"Label": "label_included", "Title": "title"}, axis=1, inplace=True)
df["doi"] = "https://doi.org/" + df["DOI"].str.extract(r"(10.\S+)")

# export
df.to_csv(f"{key}_raw.csv", index=False)

df_new = df[["doi", "label_included"]].copy()
df_new["openalex_id"] = None

df_new[["doi", "openalex_id", "label_included"]].to_csv(f"{key}_ids.csv", index=False)
