import pandas as pd

# # The dataset without DOI retrieval and deduplication applied:
# df = pd.read_csv("https://osf.io/download/py7ek/", usecols=['doi', 'included'])

# To process doi retrieved version use following file:
# df = pd.read_excel("https://osf.io/download/kdqu8/", usecols=['doi', 'included'])

# To process doi retrieved and deduplicated version use following file:
df = pd.read_excel("https://osf.io/download/2mwkd/")

# adjust columns
df["doi"] = "https://doi.org/" + df["doi"].str.extract(r"(10.\S+)")
df["id_type"] = "doi"

# rename columns
df.rename({"included": "label_included"}, axis=1, inplace=True)

# save results to file
df.to_csv("Brouwer_2019_raw.csv", index=False)

df_new = df[["doi", "label_included"]].copy()
df_new["openalex_id"] = None

df_new[["doi", "openalex_id", "label_included"]].to_csv(
    "Brouwer_2019_ids.csv", index=False
)
