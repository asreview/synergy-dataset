import pandas as pd

key = "Sep_2021"

df_old = pd.read_csv("https://osf.io/download/j7sfm/", sep=";")
df_new = pd.read_csv("https://osf.io/download/bz3sj/", sep=";")[["PMID", "final.inclusion.screening"]]

df_old["label_included"] = df_old['inclusie_july2020'].replace({"yes": 1, "no": 0})
df_new["label_included"] = df_new["final.inclusion.screening"].replace({"Yes": 1, "No": 0})

df = pd.concat([df_old[["PMID", "label_included"]], df_new[["PMID", "label_included"]]], axis=0)
df = df.drop_duplicates()
df["doi"] = None
df["pmid"] = "https://pubmed.ncbi.nlm.nih.gov/" + df["PMID"].astype(str)

df["openalex_id"] = None

df[["pmid", "doi", "openalex_id", "label_included"]].to_csv(f"{key}_ids.csv", index=False)
