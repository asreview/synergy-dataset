import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

#Read input
df = pd.read_excel(
    "https://zenodo.org/records/8153272/files/SBES-SEARCH-PROCESS-FINAL.xlsx?download=1",
    engine="openpyxl",
    sheet_name="First Selection in Scopus",
    skiprows = 9
)

# FT ids taken from top of First selection in Scopus page.
ft_ids = [
    119,
    344,
    353,
    389,
    528,
    698,
    933,
    937,
    43,
    97,
    188,
    236,
    237,
    313,
    366,
    368,
    698,
    52,
    194,
    220,
    338,
    33,
    232,
    905,
]

utils.rename_columns(df, title="Title", year="Year")
utils.extract_doi(df, "DOI")

df["label_included"] = [1 if x in ft_ids else 0 for x in df["Scopus ID"]]

df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Nobrega-Dos_Santos_2023", df)
