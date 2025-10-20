import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
utils.unzip(
    "https://zenodo.org/records/5775211/files/aliciagh/slr-gender-gap-stem-v1.1.zip?download=1"
)

search_scopus = pd.read_excel(
    "aliciagh-slr-gender-gap-stem-434955f/records-from-Scopus/2015-2021_scopus_full.xlsx"
)
search_wos1 = pd.read_csv(
    "aliciagh-slr-gender-gap-stem-434955f/records-from-WoS/2015-2019_WoS_raw.txt",
    sep="\t",
    header=0,
)
search_wos2 = pd.read_excel(
    "aliciagh-slr-gender-gap-stem-434955f/records-from-WoS/2019-2021_WoS_raw.xls"
)

search_scopus = utils.extract_pmid(search_scopus, "PubMed ID")
search_scopus = utils.extract_doi(search_scopus, "DOI")
search_scopus = utils.rename_columns(search_scopus, title="Title", year="Year")

search_wos1 = utils.rename_columns(search_wos1, title="TI", year="PY")
search_wos1 = utils.extract_doi(search_wos1, "DI")
search_wos1 = utils.extract_pmid(search_wos1, "PM")

search_wos2 = utils.rename_columns(
    search_wos2, title="Article Title", year="Publication Year"
)
search_wos2 = utils.extract_doi(search_wos2, "DOI")
search_wos2 = utils.extract_pmid(search_wos2, "Pubmed Id")

search = pd.concat([search_scopus, search_wos1, search_wos2])

# FT taken from paper references (semi-automated)
inclusions = [
    {"doi": "https://doi.org/10.1007/978-94-007-7793-4"},
    {"doi": "https://doi.org/10.1080/03043797.2015.1121466"},
    {"doi": "https://doi.org/10.1145/3196839.3196857"},
    {"doi": "https://doi.org/10.3390/e21010030"},
    {"doi": "https://doi.org/10.1016/j.sbspro.2015.04.569"},
    {"doi": "https://doi.org/10.1177/0162353217734374"},
    {"doi": "https://doi.org/10.1177/0016986217702215"},
    {"doi": "https://doi.org/10.1016/j.ijer.2016.11.004"},
    {"doi": "https://doi.org/10.1145/3196839.3196879"},
    {"doi": "https://doi.org/10.1080/02680513.2018.1554475"},
    {"doi": "https://doi.org/10.1103/PhysRevPhysEducRes.14.020113"},
    {"doi": "https://doi.org/10.1145/3183377.3183390"},
    {"doi": "https://doi.org/10.1109/EDUCON.2018.8363496"},
    {"doi": "https://doi.org/10.1109/EDUCON.2018.8363494"},
    {"doi": "https://doi.org/10.1080/09645292.2018.1426731"},
    {"doi": "https://doi.org/10.1145/2909824.3020242"},
    {"doi": "https://doi.org/10.1109/FIE.2015.7344113"},
    {"doi": "https://doi.org/10.1080/02635143.2017.1285760"},
    {"doi": "https://doi.org/10.1080/09500693.2018.1534021"},
    {"doi": "https://doi.org/10.1109/TE.2018.2820643"},
    {"doi": "https://doi.org/10.3389/fpsyg.2017.00703"},
    {"doi": "https://doi.org/10.1109/FIE.2016.7757680"},
    {"doi": "https://doi.org/10.1080/00131946.2017.1369085"},
    {"doi": "https://doi.org/10.1109/RITA.2020.3008114"},
    {"doi": "https://doi.org/10.1109/RITA.2020.3033231"},
    {"doi": "https://doi.org/10.1080/09589236.2021.1922272"},
]

ft = pd.DataFrame(inclusions)

# set labels and turn into single dataframe
df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Verdugo-Castro_2022", df)
