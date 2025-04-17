import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# get data
# data doi: 10.25340/R4/VB85L1 (download requires extra popup, so using downloaded file)
search = pd.read_excel("data/Ali et al datasets.xlsx", sheet_name="Toffalini")
search = utils.rename_columns(search, title="Title", ti_ab_label="Label")

# FT taken from paper references
inclusions = [
    {"doi": "https://doi.org/10.1080/10888438.2015.1108321"},
    {"doi": "https://doi.org/10.3389/fpsyg.2015.01510"},
    {"doi": "https://doi.org/10.1177/2F0022219415617163"},
    {"doi": "https://doi.org/10.1016/j.neuropsychologia.2018.03.016"},
    {"doi": "https://doi.org/10.3233/RNN-150561"},
    {"doi": "https://doi.org/10.3389/fpsyg.2016.01937"},
    {"doi": "https://doi.org/10.1177/2F0022219412450618"},
    {"doi": "https://doi.org/10.1038/s41598-018-37753-7"},
    {"doi": "https://doi.org/10.1159/000489091"},
    {"doi": "https://doi.org/10.1371/journal.pone.0138715"},
    {"doi": "https://doi.org/10.1016/j.cub.2013.01.044"},
    {"doi": "https://doi.org/10.1038/s41598-017-17626-1"},
    {"doi": "https://doi.org/10.1038/s41598-017-05826-8"},
    {"doi": "https://doi.org/10.1007/s11145-012-9418-z"},
    {"doi": "https://doi.org/10.1371/journal.pone.0143914"},
    {"doi": "https://doi.org/10.1016/j.compedu.2020.103834"},
    {"doi": "https://doi.org/10.1093/cercor/bhv206"},
    {"doi": "https://doi.org/10.1016/j.neuropsychologia.2015.02.022"},
    {"doi": "https://doi.org/10.1007/s11881-014-0093-4"},
    {"doi": "https://doi.org/10.1002/brb3.281"},
    {"doi": "https://doi.org/10.1109/isgs49501.2019.9047004"},
    {"doi": "https://doi.org/10.1177/2F0022219417711223"},
    {"doi": "https://doi.org/10.1111/1467-8578.12278"},
    {"doi": "https://doi.org/10.1080/10573569.2018.1515049"},
    {"doi": "https://doi.org/10.1016/j.jneuroling.2020.100904"},
    {"doi": "https://doi.org/10.1038/s41598-017-18878-7"},
    {"doi": "https://doi.org/10.3969/j.issn.1673-5374.2013.05.009"},
    {"doi": "https://doi.org/10.1371/journal.pone.0108274"},
    {"doi": "https://doi.org/10.1177/0022219419895261"},
    {"doi": "https://doi.org/10.1177/0022219418775114"},
    {"doi": "https://doi.org/10.3389/fpsyg.2017.01904"},
    {"doi": "https://doi.org/10.1007/s11881-019-00176-8"},
    {"doi": "https://doi.org/10.3233/RNN-190939"},
    {"doi": "https://doi.org/10.1007/s11881-014-0091-6"},
    {"doi": "https://doi.org/10.1002/dys.1529"},
    {"doi": "https://doi.org/10.1371/journal.pone.0186114"},
    {"doi": "https://doi.org/10.1038/s41598-019-55624-7"},
]

ft = pd.DataFrame(inclusions)
ft["label_abstract_included"] = 1

# set labels and turn into single dataframe
df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Toffalini_2021", df)
