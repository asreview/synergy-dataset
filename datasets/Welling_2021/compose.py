import pandas as pd

key = "Welling_2021"

df_search = pd.read_csv("https://osf.io/download/fsq9g/")
df_inclusions = pd.read_csv("https://osf.io/download/zmyp6/")


# set labels and turn into single dataframe
df_inclusions["label_included"] = 1
df_search["label_included"] = 0
df = pd.concat([df_inclusions, df_search], ignore_index=True)
df.columns = [x.lower() for x in list(df)]
df.drop_duplicates(inplace=True)

# adjust columns and drop missing and duplicate ids
df['doi'] = "https://doi.org/" + df['doi'].str.extract(r"(10.\S+)")

# save results to file
df.to_csv(f"{key}_raw.csv", index=False)

df_new = df[["doi", "label_included"]].copy()
df_new["openalex_id"] = None

df_new[["doi", "openalex_id", "label_included"]].to_csv(f"{key}_ids.csv", index=False)
