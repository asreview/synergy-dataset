import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

df_old = pd.read_csv("https://osf.io/download/j7sfm/", sep=";")
df_new = pd.read_csv("https://osf.io/download/bz3sj/", sep=";")[
    ["PMID", "final.inclusion.screening"]
]

df_old = utils.extract_labels(df_old, "inclusie_july2020", "yes")
df_new = utils.extract_labels(df_new, "final.inclusion.screening", "Yes")

df = pd.concat(
    [df_old[["PMID", "label_included"]], df_new[["PMID", "label_included"]]], axis=0
)

df = utils.extract_pmid(df, "PMID")
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Sep_2021", df)
