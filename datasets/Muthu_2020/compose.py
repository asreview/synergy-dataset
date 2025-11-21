import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

search = pd.read_csv("https://osf.io/download/v3qjd/", sep="\t", encoding="windows-1252")

# Inclusions taken from paper (they were almost all in the dataset, but not all correctly labeled)
inclusions = [
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/30215593", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/26825787", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/22314520", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/29396603", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/12811263", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/19506919", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/23321148", "doi": None},
    {"pmid": None, "doi": "https://doi.org/10.1016/j.spinee.2017.05.025"},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/20809722", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/23568254", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/21997779", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/18521599", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/21699471", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/29652784", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/19571082", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/26984911", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/19487515", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/23778373", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/21375382", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/26630435", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/19092613", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/17621221", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/26712393", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/24361998", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/23996046", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/22691917", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/24296479", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/30180054", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/19179917", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/16648739", "doi": None},
    {"pmid": None, "doi": "https://doi.org/10.1016/j.spinee.2016.11.010"},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/20651016", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/23407406", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/28735763", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/30325888", "doi": None},
    {"pmid": None, "doi": "https://doi.org/10.1007/s00586-009-1161-z"},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/23632782", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/18774751", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/21275549", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/21165658", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/24810818", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/30299415", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/25868100", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/25955086", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/23591659", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/19287352", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/19148687", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/17224800", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/18758356", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/22310097", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/24480956", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/19442011", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/14722400", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/28207654", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/23893083", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/23403549", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/19412139", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/29730458", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/23804157", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/20670575", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/24335723", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/29110696", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/22173608", "doi": None},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/23080427", "doi": None},
    {"pmid": None, "doi": "https://doi.org/10.1002/jbmr.1564"},
    {"pmid": None, "doi": "https://doi.org/10.1097/bpo.0b013e3181b2ba08"},
    {"pmid": None, "doi": "https://doi.org/10.1056/nejmoa0900563"},
    {"pmid": None, "doi": "https://doi.org/10.1097/00007632-200207010-00002"},
    {"pmid": None, "doi": "https://doi.org/10.1097/brs.0000000000000106"},
    {"pmid": None, "doi": "https://doi.org/10.1097/bsd.0b013e318201be2a"},
]

ft = pd.DataFrame(inclusions)

search = utils.extract_doi(search, "Url", "https://doi.org/")
search = utils.extract_pmid(search, "Url", "https://pubmed.ncbi.nlm.nih.gov/")
search = utils.rename_columns(search, title="Title", year="Publication Year", abstract="Abstract Note", authors="Author")

df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Muthu_2020", df)
