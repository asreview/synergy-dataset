import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

df_labels = pd.read_excel("https://osf.io/gmvxy/download")
df_abstracts = pd.read_excel("https://osf.io/5zw46/download")

df_labels["title"] = df_labels["Title"]
df_labels["label_included"] = (
    df_labels["Final Decision"].str.startswith("Include")
).astype(int)
df_labels["label_abstract_included"] = 1

df = pd.merge(
    df_abstracts,
    df_labels.reindex(columns=["title", "label_included", "label_abstract_included"]),
    how="left",
    on="title",
)

df = utils.extract_doi(df, "url", "", "&")
df["label_included"] = df["label_included"].fillna(0).astype(int)
df["label_abstract_included"] = df["label_abstract_included"].fillna(0).astype(int)

df = utils.drop_duplicates(df)

# save results to file
utils.write_ids_files("Moran_2020", df)
