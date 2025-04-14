import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# get data
# data doi: 10.25340/R4/VB85L1 (download requires extra popup, so using downloaded file)
search = pd.read_excel("data/Ali et al datasets.xlsx", sheet_name="Clark")
search = utils.rename_columns(search, title="Title", ti_ab_label="Label")

# FT taken from paper references
inclusions = [
    {"doi": "https://doi.org/10.1044/2019_LSHSS-VOIA-18-0138"},
    {"doi": "https://doi.org/10.1044/2018_JSLHR-L-17-0336"},
    {"doi": "https://doi.org/10.1080/17470218.2013.859714"},
    {"doi": "https://doi.org/10.1017/S0305000912000396"},
    {"doi": "https://doi.org/10.1016/j.jecp.2015.01.015"},
]

ft = pd.DataFrame(inclusions)
ft["label_abstract_included"] = 1

# set labels and turn into single dataframe
df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Clark_2021", df)
