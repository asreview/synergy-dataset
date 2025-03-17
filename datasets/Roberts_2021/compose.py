import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# get search
search = pd.read_csv("https://osf.io/b6sqt/download")
search.rename(columns={"label_included": "label_abstract_included"}, inplace=True)
search = utils.extract_doi(search, "DOI")

# FT taken from paper references
inclusions = [
    {"doi": "https://doi.org/10.1177/0022219409355475"},
    {"doi": "https://doi.org/10.1080/19345747.2012.706694"},
    {"doi": "https://doi.org/10.1080/19345747.2014.906010"},
    {"doi": "https://doi.org/10.1037/a0032581"},
    {"doi": "https://doi.org/10.1080/02796015.2011.12087720"},
    {"doi": "https://doi.org/10.1177/0014402918802801"},
    {"doi": "https://doi.org/10.1044/2014_LSHSS-13-0008"},
    {"doi": "https://doi.org/10.1177/1525740114548917"},
    {"doi": "https://doi.org/10.1177/0265659009349985"},
    {"doi": "https://doi.org/10.1080/19388070902875173"},
    {"doi": "https://doi.org/10.1177/0022219409355472"},
    {"doi": "https://doi.org/10.1080/09362835.2014.865952"},
    {"doi": "https://doi.org/10.1177%2F001440291107700204"},
    {"doi": "https://doi.org/10.1177/00222194070400040401"},
    {"doi": "https://doi.org/10.1080/19345747.2017.1375582"},
    {"doi": "https://doi.org/10.1177/0022219409338742"},
    {"doi": "https://doi.org/10.1007/s11145-008-9119-9"},
    {"doi": "https://doi.org/10.1080/10888430903162894"},
    {"doi": "https://doi.org/10.1037/a0019639"},
    {"doi": "https://doi.org/10.1037/0022-0663.98.3.508"},
    {"doi": "https://doi.org/10.1177/07419325060270060601"},
    {"doi": "https://doi.org/10.1177/00222194070400060301"},
    {"doi": "https://doi.org/10.1080/02568543.2017.1418771"},
    {"doi": "https://doi.org/10.1080/00220671.2017.1393650"},
]

ft = pd.DataFrame(inclusions)
ft["label_abstract_included"] = 1

# set labels and turn into single dataframe
df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Roberts_2021", df)
