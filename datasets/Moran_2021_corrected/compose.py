import pandas as pd

key = "Moran_2021_corrected"

df_labels = pd.read_excel("https://osf.io/gmvxy/download")
df_abstracts = pd.read_excel("https://osf.io/5zw46/download")

df_labels["title"] = df_labels["Title"]
df_labels["label_included"] = (df_labels["Final Decision"].str.startswith("Include")).astype(int)
df_labels["label_abstract_included"] = 1
df_labels = df_labels.reindex(columns=["title", "label_included", "label_abstract_included"])

df = pd.merge(df_abstracts, df_labels, how="outer", on="title")

df["doi"] = "https://doi.org/" + df["url"].str.extract(r"(10\.[^&]*)")[0]
df['label_included'] = df['label_included'].fillna(0).astype(int)
df['label_abstract_included'] = df['label_abstract_included'].fillna(0).astype(int)

# save results to file
df.to_csv(f"{key}_raw.csv", index=False)
df.reindex(columns=["openalex_id", "doi", "label_included", "label_abstract_included", "method"]).to_csv(f"{key}_ids.csv", index=False)
