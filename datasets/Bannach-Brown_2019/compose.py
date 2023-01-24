import pandas as pd

key = "Bannach-Brown_2019"

url = "https://zenodo.org/record/151190/files/Depression-Dataset-SLIM-DevelopmentTrainingSet.txt"
df = pd.read_table(url, index_col="ID")

# rename columns
df.rename(
    columns={"Incl(1)/Excl(0)": "label_included", "Author": "authors"}, inplace=True
)
df.columns = map(str.lower, df.columns)

# adjust columns
df["doi"] = None

# export
df.to_csv(f"{key}_raw.csv", index=False)

df_new = df[["doi", "label_included"]].copy()
df_new["openalex_id"] = None

df_new[["doi", "openalex_id", "label_included"]].to_csv(f"{key}_ids.csv", index=False)
