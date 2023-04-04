import pandas as pd
from asreview import ASReviewData

key = "van_Dis_2020"

# load RIS into ASReviewData object
asr_inclusions = ASReviewData.from_file("https://osf.io/vuyhq/download")
asr_search = ASReviewData.from_file("https://osf.io/3grcz/download")
asr_search.df.rename({"\ufeffTitle": "Title"}, axis=1, inplace=True)

# set labels and turn into single dataframe
asr_inclusions.df["label_included"] = 1
asr_search.df["label_included"] = 0
df = pd.concat([asr_inclusions.df, asr_search.df], ignore_index=True)
df.drop_duplicates(inplace=True)

# adjust columns and drop missing and duplicate ids
df["doi"] = "https://doi.org/" + df["DOI"].str.extract(r"(10.\S+)")

# fix broken DOI that break openalex/pyalex
df.loc[
    df["doi"] == "https://doi.org/10.1002/(SICI)1097-0134(199606)25:2&lt", "doi"
] = "https://doi.org/10.1002/(SICI)1097-0134(199606)25:2<215::AID-PROT7>3.0.CO;2-G"

df.rename({"Title": "title", "Published Year": "year"}, axis=1, inplace=True)

df["pmid"] = None
pubmed = df["Ref"].notnull() & (df["Ref"].str.len() <= 8)
df.loc[pubmed, "pmid"] = "https://pubmed.ncbi.nlm.nih.gov/" + df.loc[pubmed, "Ref"]

# save results to file
df.to_csv(f"{key}_raw.csv", index=False)

df_new = df[["pmid", "doi", "label_included"]].copy()
df_new["openalex_id"] = None

df_new[["pmid", "doi", "openalex_id", "label_included"]].to_csv(
    f"{key}_ids.csv", index=False
)
