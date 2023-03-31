import pandas as pd
from asreview import ASReviewData

import urllib.parse


key = "Leenaars_2020"


def unquote_nan(x):
    try:
        return urllib.parse.unquote(urllib.parse.unquote(x))
    except Exception:
        return None

# load RIS files into ASReviewData object
df_pubmed = ASReviewData.from_file("https://osf.io/download/435yd/").df
df_embase = ASReviewData.from_file("https://osf.io/download/q2bca/").df
df_inclusions = pd.read_excel("https://osf.io/download/r94qm/", sheet_name="FT_included")[["title"]]
df_inclusions["label_included"] = 1

df_pubmed["pmid"] = None
df_pubmed.loc[df_pubmed["accession_number"].notnull(), "pmid"] = "https://pubmed.ncbi.nlm.nih.gov/" + df_pubmed.loc[df_pubmed["accession_number"].notnull(), "accession_number"]

df_embase["doi"] = df_embase["url"].str.extract(r"doi\/(10.\S+?)&")[0].apply(unquote_nan)
df_embase["pmid"] = "https://pubmed.ncbi.nlm.nih.gov/" + df_embase["url"].str.extract(r"pmid\/(\d+)&")[0]

# set labels and turn into single dataframe
df = pd.concat([df_pubmed, df_embase], ignore_index=True)
df = df.merge(df_inclusions, on="title", how="left")
df.loc[df["label_included"].isnull(), "label_included"] = 0
df["label_included"] = df["label_included"].astype(int)

# adjust columns and drop missing and duplicate ids
df["doi"] = "https://doi.org/" + df["doi"].str.extract(r"(10.\S+)")
df["doi"] = df["doi"].str.split("&", n = 1, expand = True)[0]

# save results to file
df.to_csv(f"{key}_raw.csv", index=False)

df_new = df[["pmid", "doi", "label_included"]].copy()
df_new["openalex_id"] = None

df_new[["pmid", "doi", "openalex_id", "label_included"]].to_csv(f"{key}_ids.csv", index=False)
