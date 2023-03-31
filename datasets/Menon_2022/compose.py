import pandas as pd

key = "Menon_2022"

df_exclusions = pd.read_csv("https://osf.io/download/y83tu/").rename(
    {"pubmed_id": "pmid"}, axis=1
)
df_inclusions = pd.read_excel("https://osf.io/download/mgxwj/").rename(
    {"DOI name": "doi", "PubMed ID": "pmid"}, axis=1
)

# set labels and turn into single dataframe
df_inclusions["label_included"] = 1
df_exclusions["label_included"] = 0
df = pd.concat([df_inclusions, df_exclusions], ignore_index=True)
df.rename({"Title": "title"}, axis=1, inplace=True)

# save results to file
df.to_csv(f"{key}_raw.csv", index=False)

df["doi"] = "https://doi.org/" + df["doi"]
df["pmid"] = "https://pubmed.ncbi.nlm.nih.gov/" + df["pmid"].astype(str)


df_new = df[["pmid", "doi", "label_included"]].copy()
df_new["openalex_id"] = None

df_new[["pmid", "doi", "openalex_id", "label_included"]].to_csv(
    f"{key}_ids.csv", index=False
)
