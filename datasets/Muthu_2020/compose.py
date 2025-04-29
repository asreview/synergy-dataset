import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

search = pd.read_csv("https://osf.io/download/v3qjd/", sep="\t", encoding="windows-1252")

# Inclusions taken from paper (they were almost all in the dataset, but not all correctly labeled)
inclusions = [
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/30215593", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/26825787", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/22314520", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/29396603", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/12811263", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/19506919", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/23321148", "doi": None},
    {"pmid": None, "doi": "https://doi.org/10.1016/j.spinee.2017.05.025"},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/20809722", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/23568254", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/21997779", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/18521599", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/21699471", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/29652784", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/19571082", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/26984911", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/19487515", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/23778373", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/21375382", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/26630435", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/19092613", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/17621221", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/26712393", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/24361998", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/23996046", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/22691917", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/24296479", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/30180054", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/19179917", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/16648739", "doi": None},
    {"pmid": None, "doi": "https://doi.org/10.1016/j.spinee.2016.11.010"},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/20651016", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/23407406", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/28735763", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/30325888", "doi": None},
    {"pmid": None, "doi": "https://doi.org/10.1007/s00586-009-1161-z"},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/23632782", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/18774751", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/21275549", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/21165658", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/24810818", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/30299415", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/25868100", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/25955086", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/23591659", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/19287352", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/19148687", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/17224800", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/18758356", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/22310097", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/24480956", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/19442011", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/14722400", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/28207654", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/23893083", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/23403549", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/19412139", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/29730458", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/23804157", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/20670575", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/24335723", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/29110696", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/22173608", "doi": None},
    {"pmid": "https://www.ncbi.nlm.nih.gov/pubmed/23080427", "doi": None},
    {"pmid": None, "doi": "https://doi.org/10.1002/jbmr.1564"},
    {"pmid": None, "doi": "https://doi.org/10.1097/bpo.0b013e3181b2ba08"},
    {"pmid": None, "doi": "https://doi.org/10.1056/nejmoa0900563"},
    {"pmid": None, "doi": "https://doi.org/10.1097/00007632-200207010-00002"},
    {"pmid": None, "doi": "https://doi.org/10.1097/brs.0000000000000106"},
    {"pmid": None, "doi": "https://doi.org/10.1097/bsd.0b013e318201be2a"},
]

ft = pd.DataFrame(inclusions)

search = utils.extract_doi(search, "Url", "https://doi.org/")
search = utils.extract_pmid(search, "Url", "https://www.ncbi.nlm.nih.gov/pubmed/")
search = utils.rename_columns(search, title="Title", year="Publication Year")

df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Muthu_2020", df)
