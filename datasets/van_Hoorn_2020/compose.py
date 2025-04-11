import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# get data
# data doi: 10.25340/R4/VB85L1 (download requires extra popup, so using downloaded file)
search = pd.read_excel("data/Ali et al datasets.xlsx", sheet_name="VanHoorn")
search = utils.rename_columns(search, title="Title", ti_ab_label="Label")

# FT taken from paper references
inclusions = [
    {"openalex_id": "https://openalex.org/W2132495906"},
    {"openalex_id": "https://openalex.org/W2097258174"},
    {"openalex_id": "https://openalex.org/W1983561697"},
    {"openalex_id": "https://openalex.org/W2130189613"},
    {"openalex_id": "https://openalex.org/W2120417672"},
    {"openalex_id": "https://openalex.org/W2139049878"},
    {"openalex_id": "https://openalex.org/W2766373333"},
    {"openalex_id": "https://openalex.org/W2805078484"},
    {"openalex_id": "https://openalex.org/W2090831264"},
    {"openalex_id": "https://openalex.org/W1986420863"},
    {"openalex_id": "https://openalex.org/W2154365911"},
    {"openalex_id": "https://openalex.org/W2568029334"},
    {"openalex_id": "https://openalex.org/W2077603433"},
    {"openalex_id": "https://openalex.org/W2523747929"},
    {"openalex_id": "https://openalex.org/W2057460417"},
    {"openalex_id": "https://openalex.org/W2475206885"},
    {"openalex_id": "https://openalex.org/W2168004369"},
    {"openalex_id": "https://openalex.org/W2792131382"},
    {"openalex_id": "https://openalex.org/W2079662966"},
    {"openalex_id": "https://openalex.org/W2007069516"},
    {"openalex_id": "https://openalex.org/W2125138580"},
    {"openalex_id": "https://openalex.org/W2324433786"},
    {"openalex_id": "https://openalex.org/W2035723040"},
    {"openalex_id": "https://openalex.org/W2154000541"},
    {"openalex_id": "https://openalex.org/W2285498898"},
    {"openalex_id": "https://openalex.org/W1607383675"},
    {"openalex_id": "https://openalex.org/W2054372021"},
    {"openalex_id": "https://openalex.org/W2280076594"},
    {"openalex_id": "https://openalex.org/W2908553537"},
    {"openalex_id": "https://openalex.org/W2013075372"},
    {"openalex_id": "https://openalex.org/W2025365343"},
    {"openalex_id": "https://openalex.org/W2126683967"},
    {"openalex_id": "https://openalex.org/W1514022073"},
    {"openalex_id": "https://openalex.org/W2113427618"},
    {"openalex_id": "https://openalex.org/W2162947206"},
    {"openalex_id": "https://openalex.org/W2148569480"},
    {"openalex_id": "https://openalex.org/W2800343843"},
    {"openalex_id": "https://openalex.org/W1976901552"},
]

ft = pd.DataFrame(inclusions)
ft["label_abstract_included"] = 1

# set labels and turn into single dataframe
df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("van_Hoorn_2020", df)
