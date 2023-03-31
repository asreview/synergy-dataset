import pandas as pd
from asreview import ASReviewData

key = "Oud_2018"

# load RIS into ASReviewData object
asr_all = ASReviewData.from_file("https://osf.io/download/7shuv/?view_only=f30f6eb898e24a6f8a19734e8b1fc19b")
df = asr_all.df.rename({"included": "label_included"}, axis=1)

# adjust columns and drop missing and duplicate ids
df["doi"] = "https://doi.org/" + df["doi"].str.extract(r"(10.\S+)")

# save results to file
df.to_csv(f"{key}_raw.csv", index=False)

df_new = df[["doi", "label_included"]].copy()
df_new["openalex_id"] = None

df_new[["doi", "openalex_id", "label_included"]].to_csv(f"{key}_ids.csv", index=False)
