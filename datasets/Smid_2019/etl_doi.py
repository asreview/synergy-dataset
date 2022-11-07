import pandas as pd

df = pd.read_csv("https://osf.io/download/gxams/", usecols=['doi', 'included'])

# adjust columns
df["doi"] = df["doi"].str.extract(r"(10.\S+)")
df['id_type'] = 'doi'

# rename columns
df.rename({'included': 'label_included', 'doi': 'id'}, axis=1, inplace=True)

# drop missing ids
df.dropna(subset=["id"], inplace=True)

# drop duplicate DOIs
df.drop_duplicates(subset=['id'])

# export
df.to_csv("Smid_2019_ids.csv", columns=['id', 'id_type', 'label_included'], index=False)
