import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
search = pd.read_excel(
    "https://zenodo.org/records/6363744/files/dataset_plosone.xlsx?download=1",
    skiprows=2,
)

# FT taken from paper references
inclusions = [
    {"doi": "https://doi.org/10.1016/j.abb.2004.03.030"},
    {"doi": "https://doi.org/10.1002/dmrr.601"},
    {"doi": "https://doi.org/10.1002/tox.22130"},
    {"doi": "https://doi.org/10.1385/bter:105:1-3:135"},
    {"doi": "https://doi.org/10.1007/s12011-014-0076-7"},
    {"doi": "https://doi.org/10.1007/s12011-014-9952-4"},
    {"doi": "https://doi.org/10.1016/S0753-3322(98)80008-5"},
    {"doi": "https://doi.org/10.1007/s12011-012-9401-1"},
    {"doi": "https://doi.org/10.1385/BTER:99:1-3:241"},
    {"doi": "https://doi.org/10.1385/BTER:103:3:207"},
    {"doi": "https://doi.org/10.2147/IJN.S91377"},
    {"doi": "https://doi.org/10.1016/j.heliyon.2020.e04045"},
    {"doi": "https://doi.org/10.1177/0960327115579207"},
]

ft = pd.DataFrame(inclusions)

# Process data
search = utils.extract_doi(search, "url", "doi=", "&")
search = utils.extract_pmid(search, "pubmed_id")
search = utils.extract_pmid(search, "url", "https://pubmed.ncbi.nlm.nih.gov/")

df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Ferreira_2022", df)
