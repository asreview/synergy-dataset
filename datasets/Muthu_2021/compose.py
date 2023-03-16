import pandas as pd

key = "Muthu_2021"

df = pd.read_csv("https://osf.io/download/v3qjd/", sep="\t", encoding="windows-1252")

# adjust columns
dois = df["Url"].str.startswith("https://doi.org")
df.loc[dois, "doi"] = df.loc[dois, "Url"]
df["Url"] = df["Url"].str.replace("https://www.ncbi.nlm.nih.gov/pubmed/", "https://pubmed.ncbi.nlm.nih.gov/", regex=False)
pmids = df["Url"].str.startswith("https://pubmed.ncbi.nlm.nih.gov")
df.loc[pmids, "pmid"] = df.loc[pmids, "Url"]

# rename columns
df.rename({"Label": "label_included", "Title": "title"}, axis=1, inplace=True)

# export
df.to_csv(f"{key}_raw.csv", index=False)

df_new = df[["pmid", "doi", "label_included"]].copy()
df_new["openalex_id"] = None

df_new[["pmid", "doi", "openalex_id", "label_included"]].to_csv(f"{key}_ids.csv", index=False)
