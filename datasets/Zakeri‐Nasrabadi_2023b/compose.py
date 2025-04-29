import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
sheets = pd.read_excel(
    "https://zenodo.org/records/7993619/files/slr_papers_R3_v3.xlsx?download=1",
    engine="openpyxl",
    sheet_name=None,
)

search = sheets["initial-articles"]
tiab = sheets["initial-selection"]
ft = sheets["final-selected"]

search = utils.rename_columns(search, title="Article title", year="Year")
tiab = utils.rename_columns(tiab, title="Article title", year="Year")
ft = utils.rename_columns(ft, title="Article title", year="Year")

df = utils.combine_datafiles(search, ft, tiab)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Zakeri‐Nasrabadi_2023b", df)
