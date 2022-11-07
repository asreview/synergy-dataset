import pandas as pd

# The dataset without DOI retrieval and deduplication applied:
df = pd.read_csv("https://osf.io/download/py7ek/", usecols=['doi', 'included'])

# To process doi retrieved version use following file:
# df = pd.read_excel("https://osf.io/download/kdqu8/", usecols=['doi', 'included'])

# To process doi retrieved and deduplicated version use following file:
# df = pd.read_excel("https://osf.io/download/2mwkd/", usecols=['doi', 'included'])

# adjust columns
df["doi"] = df["doi"].str.extract(r"(10.\S+)")
df['id_type'] = 'doi'

# rename columns
df.rename({'included': 'label_included', 'doi': 'id'}, axis=1, inplace=True)

# drop missing ids
df.dropna(subset=["id"], inplace=True)

# drop duplicate DOIs
df.drop_duplicates(subset=['id'], inplace=True)

# export
df.to_csv("Brouwer_2019_ids.csv", columns=['id', 'id_type', 'label_included'], index=False)