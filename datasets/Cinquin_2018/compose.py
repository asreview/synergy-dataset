import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# get data
# data doi: 10.25340/R4/VB85L1 (download requires extra popup, so using downloaded file)
search = pd.read_excel("data/Ali et al datasets.xlsx", sheet_name="Pierre-Antoine")
search = utils.rename_columns(search, title="Title", ti_ab_label="Label")

# FT taken from paper references
inclusions = [
    {"openalex_id": "https://openalex.org/W2612866199"},
    {"openalex_id": "https://openalex.org/W2044842795"},
    {"openalex_id": "https://openalex.org/W2154739415"},
    {"openalex_id": "https://openalex.org/W1812868705"},
    {"openalex_id": "https://openalex.org/W2054575423"},
    {"openalex_id": "https://openalex.org/W2494948277"},
    {"openalex_id": "https://openalex.org/W2003645097"},
    {"openalex_id": "https://openalex.org/W1964069484"},
    {"openalex_id": "https://openalex.org/W1565440654"},
    {"openalex_id": "https://openalex.org/W2064975883"},
    {"openalex_id": "https://openalex.org/W2028535010"},
    {"openalex_id": "https://openalex.org/W2106262139"},
    {"openalex_id": "https://openalex.org/W2165189772"},
    {"openalex_id": "https://openalex.org/W2484185914"},
    {"openalex_id": "https://openalex.org/W2005166570"},
    {"openalex_id": "https://openalex.org/W2577028479"},
    {"openalex_id": "https://openalex.org/W1567766206"},
    {"openalex_id": "https://openalex.org/W2109732433"},
    {"openalex_id": "https://openalex.org/W2023476219"},
    {"openalex_id": "https://openalex.org/W1977551932"},
    {"openalex_id": "https://openalex.org/W2501957138"},
    {"openalex_id": "https://openalex.org/W2098611145"},
    {"openalex_id": "https://openalex.org/W2034345673"},
    {"openalex_id": "https://openalex.org/W1994839612"},
    {"openalex_id": "https://openalex.org/W1986170737"},
    {"openalex_id": "https://openalex.org/W2534340424"},
    {"openalex_id": "https://openalex.org/W2559337190"},
]

ft = pd.DataFrame(inclusions)
ft["label_abstract_included"] = 1

# set labels and turn into single dataframe
df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Cinquin_2018", df)
