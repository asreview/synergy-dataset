import pandas as pd
from asreview import ASReviewData

key = "Wolters_2018"

# load RIS into ASReviewData object
asr_inclusions = ASReviewData.from_file("https://osf.io/hy8qe/download")
asr_search = ASReviewData.from_file("https://osf.io/a26sz/download")

# set labels and turn into single dataframe
asr_inclusions.df["label_included"] = 1
asr_search.df["label_included"] = 0
df = pd.concat([asr_inclusions.df, asr_search.df], ignore_index=True)
df.drop_duplicates(inplace=True)

# adjust columns and drop missing and duplicate ids
df["doi"] = "https://doi.org/" + df["url"].str.extract(r"(10.\S+)")

df["pmid"] = None
pubmed = df["accession_number"].notnull() & (df["accession_number"].str.startswith("CN") == False)
df.loc[pubmed, "pmid"] = "https://pubmed.ncbi.nlm.nih.gov/" + df.loc[pubmed, "accession_number"]

# save results to file
df.to_csv(f"{key}_raw.csv", index=False)

df_new = df[["pmid", "doi", "label_included"]].copy()
df_new["openalex_id"] = None

df_new[["pmid", "doi", "openalex_id", "label_included"]].to_csv(f"{key}_ids.csv", index=False)
