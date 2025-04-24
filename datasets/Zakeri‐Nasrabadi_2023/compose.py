import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
sheets = pd.read_excel(
    "https://zenodo.org/records/7533578/files/smell_datasets_slr__article_selection_R1_v3.xlsx?download=1",
    engine="openpyxl",
    sheet_name=None,
)

search = sheets["All"]
tiab = sheets["exclusion_passed"]
ft = sheets["inclusion-passed"]

search = utils.rename_columns(search, title="Title")
tiab = utils.rename_columns(tiab, title="Title")
ft = utils.rename_columns(ft, title="Titles")

df = utils.combine_datafiles(search, ft, tiab)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Zakeri‐Nasrabadi_2023", df)
