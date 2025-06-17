import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
sheets = pd.read_excel(
    "https://zenodo.org/records/6635964/files/SLR%20DOST%20replication%20package%20for%20publication.xlsx?download=1",
    engine="openpyxl",
    sheet_name=None,
)

search = sheets["1 2 combined"]
tiab = sheets["included 1st"]

# Note: the doi's in the urls do not correspond with the titles, so are not used.

search = utils.rename_columns(search, title="Title", year="Year")
tiab = utils.rename_columns(tiab, title="Title", year="Year")
ft = tiab[tiab["IN/OUT decision"] == "included"].copy()

df = utils.combine_datafiles(search, ft, tiab)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Deckers_2022", df)
