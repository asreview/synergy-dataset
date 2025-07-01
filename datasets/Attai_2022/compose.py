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

exclusions = sheets["Exclude_Papers"]
ft = sheets["Included_Papers"]

exclusions = utils.rename_columns(exclusions, title="Title")
ft = utils.rename_columns(ft, title="Title", year="Year")

df = utils.combine_datafiles(exclusions, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Attai_2022", df)
