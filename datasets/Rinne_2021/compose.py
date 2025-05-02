import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
search = pd.read_excel(
    "https://zenodo.org/records/5184745/files/Supplement_4.xlsx?download=1"
)
ft = pd.read_excel(
    "https://zenodo.org/records/5184745/files/Supplement_3.xlsx?download=1"
)

search = utils.rename_columns(search, title="Unnamed: 2", year="Unnamed: 3")
search = search.iloc[1:]
ft = utils.rename_columns(ft, title="Unnamed: 2", year="Unnamed: 3")
ft = ft.iloc[2:]

df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Rinne_2021", df)
