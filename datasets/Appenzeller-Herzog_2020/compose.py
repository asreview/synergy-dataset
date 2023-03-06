import pandas as pd
from asreview import ASReviewData

key = "Appenzeller-Herzog_2020"

# load RIS into ASReviewData object
asr_inclusions = ASReviewData.from_file(
    "https://zenodo.org/record/3625931/files/DOKU_All%20Included_20200116_cap.txt"
)
asr_search = ASReviewData.from_file(
    "https://zenodo.org/record/3625931/files/DOKU_All%20TiAb-Screening_20200116_cap.txt"
)

# set labels and turn into single dataframe
asr_inclusions.df["label_included"] = 1
asr_search.df["label_included"] = 0
df = pd.concat([asr_inclusions.df, asr_search.df], ignore_index=True)
df.drop_duplicates(inplace=True)

# adjust columns and drop missing and duplicate ids
df["doi"] = "https://doi.org/" + df["doi"].str.extract(r"(10.\S+)")
df["pmid"] = "https://pubmed.ncbi.nlm.nih.gov/" + df["url"].str.extract(r"id\=pmid\:(\d+)")

# save results to file
df.to_csv(f"{key}_raw.csv", index=False)

df_new = df[["doi", "pmid", "label_included"]].copy()
df_new["openalex_id"] = None

df_new[["doi", "pmid", "openalex_id", "label_included"]].to_csv(f"{key}_ids.csv", index=False)
