import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
search_1 = pd.read_excel(
    "https://zenodo.org/records/1188978/files/allReturnedMaterial2000-2013.xls?download=1",
    skiprows=7,
)
search_2 = pd.read_excel(
    "https://zenodo.org/records/1188978/files/allReturnedMaterial2014-2015.xls?download=1",
    skiprows=7,
)
search_3 = pd.read_excel(
    "https://zenodo.org/records/1188978/files/allReturnedMaterial2016-2017.xls?download=1",
    skiprows=7,
)
search_4 = pd.read_excel(
    "https://zenodo.org/records/1188978/files/allReturnedMaterial2017_FromAugustToJanuary2018.xls?download=1",
    skiprows=7,
)
search_5 = pd.read_excel(
    "https://zenodo.org/records/1188978/files/allReturnedMaterial2000-2017_onlyForAntipatternTerm.xls?download=1",
    skiprows=7,
)
ft_ids = pd.read_excel(
    "https://zenodo.org/records/1188978/files/IDsPrimaryStudies_SpreadsheetsAndPaper.xlsx?download=1",
    skiprows=1,
)

search = pd.concat([search_1, search_2, search_3, search_4, search_5])

search = utils.extract_doi(search, "DOI")
search["URL"] = search["URL"].replace(to_replace=r"\\", value="", regex=True)
search = utils.extract_doi(search, "URL", "doi=", "&")
search = utils.rename_columns(search, title="Title", year="Year")

ft_ids["label_included"] = 1

df = search.join(ft_ids.set_index("In this Spreadsheet"), on="ID Paper")
df = df.sort_values(by=["label_included"])
df['label_included'] = df['label_included'].fillna(value=0)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Santos_2018", df)
