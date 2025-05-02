import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
sheets = pd.read_excel(
    "https://zenodo.org/records/8242657/files/SLR_Dataset.xlsx?download=1",
    engine="openpyxl",
    sheet_name=None,
)

search = sheets["ReviewByTitle"]
df = sheets["ReviewAndRevisionByFullText"]

search = utils.rename_columns(search, title="Title", year="Year")
search = utils.extract_doi(search, "URL", "", "&")
search["label_included"] = 0
search["label_abstract_included"] = 0

df = utils.rename_columns(df, title="Title", year="Year")
df = utils.extract_doi(df, "URL", "", "&")
df["label_included"] = df["Exclusion Criteria by Title"].isnull()
df["label_abstract_included"] = 1

df = pd.concat([df, search])
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Chueca_2023", df)
