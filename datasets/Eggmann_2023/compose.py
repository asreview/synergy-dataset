import pandas as pd
from bibReader.frame import bReader
import sys

sys.path.append("../../scripts")
import utils

# read_input
bib = bReader()  # instantiate bReader class
bib.load(
    source="https://zenodo.org/records/7662400/files/1296%20records%20identified%20through%20electronic%20database%20searches_eggmann%202023.bib?download=1"
)
bib.fit()
search = bib.df

search = utils.extract_doi(search, "doi", "", "", True)

inclusions = [
    {"pmid": "", "doi": "https://doi.org/10.1007/s00520-012-1414-y"},
    {"pmid": "", "doi": "https://doi.org/10.1007/s00520-019-04782-5"},
    {"pmid": "", "doi": "https://doi.org/10.1007/s00784-013-1155-4"},
    {"pmid": "", "doi": "https://doi.org/10.1007/s00784-017-2165-4"},
    {"pmid": "", "doi": "https://doi.org/10.1016/j.ajodo.2015.03.025"},
    {"pmid": "", "doi": "https://doi.org/10.1016/j.joen.2009.01.010"},
    {"pmid": "", "doi": "https://doi.org/10.1017/s1460396919001055"},
    {"pmid": "", "doi": "https://doi.org/10.1017/s1460396921000492"},
    {"pmid": "", "doi": "https://doi.org/10.1046/j.1365-2842.2001.00758.x"},
    {"pmid": "", "doi": "https://doi.org/10.1080/09553002.2020.1741718"},
    {"pmid": "", "doi": "https://doi.org/10.1111/adj.12090"},
    {"pmid": "", "doi": "https://doi.org/10.1155/2015/798972"},
    {"pmid": "", "doi": "https://doi.org/10.15517/ijds.2022.50665"},
    {"pmid": "", "doi": "https://doi.org/10.1590/0103-6440201801436"},
    {"pmid": "", "doi": "https://doi.org/10.1590/1678-7757-2016-0663"},
    {"pmid": "", "doi": "https://doi.org/10.1590/2177-6709.27.2.e2219330.oar"},
    {"pmid": "", "doi": "https://doi.org/10.2341/20-066-l"},
    {"pmid": "", "doi": "https://doi.org/10.4103/jcd.jcd_238_22"},
    {"pmid": "", "doi": "https://doi.org/10.5005/jp-journals-10024-2235"},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/32787999", "doi": ""},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/29178724", "doi": ""},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/16958285", "doi": ""},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/19701512/", "doi": ""},
]

ft = pd.DataFrame(inclusions)

df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Eggmann_2023", df)
