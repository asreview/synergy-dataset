import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Load the data
df = pd.read_excel("https://osf.io/dwxeh/download")

# Process data
df.rename(columns={"Title": "title"}, inplace=True)
df.rename(columns={"Included": "label_included"}, inplace=True)
df.rename(columns={"Year": "year"}, inplace=True)
df["year"] = df["year"].fillna(0).astype(int).astype(str)
df = df.drop(df.columns[3:12], axis=1)  
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Pinos_Cisneros_2023", df)