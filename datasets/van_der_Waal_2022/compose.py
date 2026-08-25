import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# https://www.geriatriconcology.net/article/S1879-4068(22)00231-4/fulltext#%20
# https://www.sciencedirect.com/science/article/pii/S1879406822002314

search = pd.read_excel(
    "https://zenodo.org/record/7308297/files/GERDAT012%20Literature%20search%20for%20publication%20-%20Control%20preference%20scale.xlsx?download=1"
)

inclusions = [
    {"doi": "https://doi.org/10.1002/pon.1798"},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/23558408"},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/28903664"},
    {"doi": "https://doi.org/10.1007/s13187-016-1146-7"},
    {"doi": "https://doi.org/10.1200/JCO.2011.37.7952"},
    {"doi": "https://doi.org/10.1007/s11764-013-0298-2"},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/25629892"},
    {"doi": "https://doi.org/10.1002/pon.4284"},
    {"doi": "https://doi.org/10.1371/journal.pone.0227802"},
    {"doi": "https://doi.org/10.1016/j.urolonc.2016.06.015"},
    {"doi": "https://doi.org/10.1007/s00520-017-3994-z"},
    {"doi": "https://doi.org/10.1097/DCR.0000000000000662"},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/19625082"},
    {"doi": "https://doi.org/10.1245/s10434-020-08485-8"},
    {"doi": "https://doi.org/10.1016/j.clbc.2017.11.013"},
    {"doi": "https://doi.org/10.1111/ecc.12871"},
    {"doi": "https://doi.org/10.1097/JTO.0b013e3181f1c8cb"},
    {"doi": "https://doi.org/10.1016/j.jss.2019.04.037"},
    {"doi": "https://doi.org/10.1016/j.pec.2018.05.023"},
    {"doi": "https://doi.org/10.1001/jamaoncol.2014.112"},
    {"doi": "https://doi.org/10.1038/bjc.2014.322"},
    {"doi": "https://doi.org/10.1002/pon.5545"},
    {"doi": "https://doi.org/10.1002/pon.3949"},
    {"doi": "https://doi.org/10.1016/j.pec.2020.08.044"},
    {"doi": "https://doi.org/10.1080/0284186X.2019.1679880"},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/27040845"},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/19828279"},
    {"doi": "https://doi.org/10.1038/sj.bjc.6604611"},
    {"doi": "https://doi.org/10.1007/s00520-016-3476-8"},
    {"doi": "https://doi.org/10.1200/JGO.2016.008045"},
    {"doi": "https://doi.org/10.3747/co.v17i4.527"},
    {"doi": "https://doi.org/10.1016/j.juro.2018.02.3091"},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/23182756"},
]

ft = pd.DataFrame(inclusions)

df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("van_der_Waal_2022", df)
