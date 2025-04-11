import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# get data
# data doi: 10.25340/R4/VB85L1 (download requires extra popup, so using downloaded file)
search = pd.read_excel("data/Ali et al datasets.xlsx", sheet_name="Ruggeri")
search = utils.rename_columns(search, title="Title", ti_ab_label="Label")

# FT taken from paper references
inclusions = [
    {"openalex_id": "https://openalex.org/W1977133181"},
    {"openalex_id": "https://openalex.org/W2752729050"},
    {"openalex_id": "https://openalex.org/W259030452"},
    {"openalex_id": "https://openalex.org/W944598631"},
    {"openalex_id": "https://openalex.org/W1931540373"},
    {"openalex_id": "https://openalex.org/W2154832193"},
    {"openalex_id": "https://openalex.org/W2782842766"},
    {"openalex_id": "https://openalex.org/W2102444793"},
    {"openalex_id": "https://openalex.org/W2076889518"},
    {"openalex_id": "https://openalex.org/W2156153856"},
    {"openalex_id": "https://openalex.org/W2558339434"},
    {"openalex_id": "https://openalex.org/W2885707393"},
    {"openalex_id": "https://openalex.org/W2145206707"},
    {"openalex_id": "https://openalex.org/W1998278697"},
    {"openalex_id": "https://openalex.org/W1591614276"},
    {"openalex_id": "https://openalex.org/W2621357550"},
    {"openalex_id": "https://openalex.org/W2904972163"},
    {"openalex_id": "https://openalex.org/W2905934621"},
    {"openalex_id": "https://openalex.org/W2026180203"},
    {"openalex_id": "https://openalex.org/W2470286367"},
    {"openalex_id": "https://openalex.org/W2905570243"},
    {"openalex_id": "https://openalex.org/W1983674500"},
    {"openalex_id": "https://openalex.org/W2218777236"},
    {"openalex_id": "https://openalex.org/W2782449692"},
    {"openalex_id": "https://openalex.org/W2796897582"},
    {"openalex_id": "https://openalex.org/W2050993877"},
    {"openalex_id": "https://openalex.org/W2010418015"},
    {"openalex_id": "https://openalex.org/W2317407615"},
    {"openalex_id": "https://openalex.org/W2414335335"},
    {"openalex_id": "https://openalex.org/W2787701773"},
    {"openalex_id": "https://openalex.org/W2912629270"},
    {"openalex_id": "https://openalex.org/W2549333693"},
    {"openalex_id": "https://openalex.org/W2792687493"},
    {"openalex_id": "https://openalex.org/W2793105605"},
    {"openalex_id": "https://openalex.org/W2771250504"},
    {"openalex_id": "https://openalex.org/W2756098962"},
    {"openalex_id": "https://openalex.org/W2772689875"},
    {"openalex_id": "https://openalex.org/W2902973428"},
    {"openalex_id": "https://openalex.org/W2141980396"},
    {"openalex_id": "https://openalex.org/W2775330789"},
]

ft = pd.DataFrame(inclusions)
ft["label_abstract_included"] = 1

# set labels and turn into single dataframe
df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Ruggeri_2019", df)
