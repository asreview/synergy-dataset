import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
sheets = pd.read_excel(
    "https://zenodo.org/records/7243308/files/Systematic_Literature_Review_Data.xlsx?download=1",
    engine="openpyxl",
    sheet_name=None,
)

search = sheets["Exclude_Papers"]
ft = sheets["Included_Papers"]

search = utils.rename_columns(search, title="Title")
ft = utils.rename_columns(ft, title="Title", year="Year")

df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Kingsley_2022", df)
