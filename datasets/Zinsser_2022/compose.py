import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# get search
search = pd.read_csv("https://osf.io/xg6df/download")
search.rename(columns={"label_included": "label_abstract_included"}, inplace=True)

# FT taken from paper references
inclusions = [
    {"doi": "https://doi.org/10.1177/1053815118789177"},
    {"doi": "https://doi.org/10.1016/j.jaac.2016.06.006"},
    {"doi": "https://doi.org/10.1097/IYC.0000000000000113"},
    {"doi": "https://doi.org/10.1097/00001163-200607000-00007"},
    {"doi": "https://doi.org/10.1007/s10643-020-01057-1"},
    {"doi": "https://doi.org/10.1002/imhj.21845"},
    {"doi": "https://doi.org/10.1002/imhj.21334"},
    {"doi": "https://doi.org/10.1111/chso.12228"},
    {"doi": "https://doi.org/10.4225/03/5a6d259f0b6a6"},
    {"doi": "https://doi.org/10.1016/j.evalprogplan.2019.101773"},
    {"doi": "https://doi.org/10.1007/s10826-007-9140-7"},
    {"doi": "https://doi.org/10.1111/jcpp.12430"},
    {"doi": "https://doi.org/10.1080/10409289.2020.1785267"},
    {"doi": "https://doi.org/10.1016/j.ecresq.2008.12.002"},
    {"doi": "https://doi.org/10.1177/0271121415626130"},
    {"doi": "https://doi.org/10.1016/j.chiabu.2019.104149"},
    {"doi": "https://doi.org/10.1177/0014402920949832"},
    {"doi": "https://doi.org/10.1016/j.appdev.2017.11.006"},
    {"doi": "https://doi.org/10.3102/0002831219838236"},
    {"doi": "https://doi.org/10.1002/pits.22440"},
]

ft = pd.DataFrame(inclusions)
ft["label_abstract_included"] = 1

# set labels and turn into single dataframe
df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Zinsser_2022", df)
