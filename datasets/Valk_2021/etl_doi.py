import pandas as pd

df = pd.read_excel("https://osf.io/download/gmjcv/", usecols=['DOI', 'Included_fulltext'])

# adjust columns
df["DOI"] = df["DOI"].str.extract(r"(10.\S+)")
df['id_type'] = 'doi'

# rename columns
df.rename({'Included_fulltext': 'label_included', 'DOI': 'id'}, axis=1, inplace=True)

# drop missing ids
df.dropna(subset=["id"], inplace=True)

# export
df.to_csv("Valk_2021_ids.csv", columns=['id', 'id_type', 'label_included'], index=False)