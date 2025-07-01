from asreview.data import RISReader
import pandas as pd

import sys

sys.path.append("../../scripts")
import utils

# Get input files
search_1 = RISReader.read_data(
    "https://zenodo.org/records/15063583/files/My%20EndNote%20Library_vanBallegooijen_20210409.txt?download=1"
)
search_2 = pd.read_csv(
    "https://zenodo.org/records/15063583/files/update%202024%20search%20results.csv?download=1"
)
col_names = [
    "type",
    "authors",
    "year",
    "title",
    "journal",
    "",
    "",
    "",
    "",
    "",
    "url",
    "doi",
    "",
    "abstract",
]
search_3 = pd.read_excel(
    "https://zenodo.org/records/15063583/files/vanBallegooijen_20220506_databaseSuicidepreventie.xlsx?download=1",
    header=None,
    names=col_names,
)
search = pd.concat([search_1, search_2, search_3])

ft_exclusions = pd.read_csv(
    "https://zenodo.org/records/15063583/files/review_63783_excluded_csv_20241003192320.csv?download=1"
)
ft = pd.read_csv(
    "https://zenodo.org/records/15063583/files/full_text_inclusions.csv?download=1"
)
ti_ab = pd.concat([ft, ft_exclusions])

df = utils.combine_datafiles(search, ft, ti_ab)

# Process data
df = utils.extract_title(df, "Title")
df = utils.extract_year(df, "Published Year")
df = utils.extract_year(df, "Publication Year")
df = utils.extract_doi(df, "DOI")
df = utils.extract_doi(df, "doi", "", "", True)

df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("van_Ballegooijen_2024", df)
