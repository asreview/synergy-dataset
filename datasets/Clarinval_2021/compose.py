import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# get data
df = pd.read_excel(
    "https://zenodo.org/records/4287513/files/slr_data.xlsx?download=1",
    sheet_name="Initial Search",
)
df = df[df["Unnamed: 1"] == "OK"]
df = utils.rename_columns(df, title="INTIAL SEARCH")
df = utils.extract_labels(df, "Unnamed: 2", "Keep in set")

df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Clarinval_2021", df)
