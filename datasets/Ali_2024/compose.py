import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
sheets = pd.read_excel(
    "https://zenodo.org/records/10698027/files/Primary_Secondary_search_process.xlsx?download=1",
    engine="openpyxl",
    sheet_name=None,
)
search = sheets["After removing duplicated"]
tiab = sheets["after filtering by abstract"]

ft = pd.read_excel(
    "https://zenodo.org/records/10698027/files/Primary_secondary_search_results%20(1).xlsx?download=1",
    engine="openpyxl",
    sheet_name="SearchResults_final",
)

# process data
search = utils.rename_columns(search, title="Document Title", year="Publication Year")
search = utils.extract_doi(search, "DOI")

tiab = utils.rename_columns(tiab, title="Document Title", year="Publication Year")
tiab_1 = tiab.iloc[:166, :]
tiab_2 = tiab.iloc[170:238, :]
tiab_1 = utils.extract_doi(tiab_1, "DOI")
tiab_2 = utils.extract_doi(tiab_2, "Author Keywords")
tiab = pd.concat([tiab_1, tiab_2])

# Remove separaters
ft = ft.drop([92, 93, 101, 102, 103])
ft = utils.rename_columns(ft, title="Document Title", year="Publication Year")
ft = utils.extract_doi(ft, "DOI (Unique Identifier)")

df = utils.combine_datafiles(search, ft, tiab)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Ali_2024", df)
