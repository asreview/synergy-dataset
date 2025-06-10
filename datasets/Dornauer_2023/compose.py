import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
search = pd.read_excel("https://zenodo.org/records/7698283/files/Inital%20Set.xlsx?download=1")

ft = pd.read_excel("https://zenodo.org/records/7698283/files/Initial%20Set%20Candidates.xlsx?download=1")
ft = ft[
    ft["Selection By Abstract & Summary (Exclude (EX) / Include (IC) Criteria)"] == "IC"
]

df = utils.combine_datafiles(search, ft)
df = utils.rename_columns(df, title="Title", year="Year")
df = utils.extract_doi(df, "DOI")

df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Dornauer_2023", df)
