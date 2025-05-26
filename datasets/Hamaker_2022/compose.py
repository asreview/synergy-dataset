import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
sheets = pd.read_excel(
    "https://zenodo.org/records/7143942/files/GERDAT011%20Literature%20search%20for%20publication%20-%20Geriatric%20assessment%20in%20the%20management%20of%20older%20patients%20with%20cancer%20%E2%80%93%20a%20systematic%20review%20(update).xlsx?download=1",
    engine="openpyxl",
    sheet_name=None,
    header=None,
)

search_in = sheets["excluded"]

search_1 = search_in.iloc[:1552, :].copy()
search_1.columns = [
    "authors",
    "title",
    "A",
    "B",
    "C",
    "D",
    "E",
    "pubmed2",
    "F",
    "link",
    "H",
    "I",
    "pubmed1",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "p",
]
search_1["pubmed1"] = search_1["pubmed1"].astype("string")
search_1["pubmed2"] = search_1["pubmed2"].astype("string")
search_1 = utils.extract_pmid(search_1, "pubmed1", "", False, True)
search_1 = utils.extract_pmid(search_1, "pubmed2", "", False, True)
search_1 = utils.extract_doi(search_1, "link")
search_1 = utils.extract_doi(search_1, "pubmed1")

search_2 = search_in.iloc[1619:].copy()
search_2.columns = [
    "authors",
    "title",
    "A",
    "B",
    "C",
    "D",
    "link",
    "link2",
    "link3",
    "link4",
    "link5",
    "pubmed1",
    "pubmed2",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
]
search_2["pubmed1"] = search_2["pubmed1"].astype("string")
search_2["pubmed2"] = search_2["pubmed2"].astype("string")

search_2 = utils.extract_doi(search_2, "link", "", "&")
search_2 = utils.extract_doi(search_2, "link2", "", "&")
search_2 = utils.extract_doi(search_2, "link3", "", "&")
search_2 = utils.extract_doi(search_2, "link4", "", "&")
search_2 = utils.extract_doi(search_2, "link5", "", "&")
search_2 = utils.extract_doi(search_2, "pubmed2", "", "&")
search_2 = utils.extract_pmid(search_2, "pubmed1", "", False, True)
search_2 = utils.extract_pmid(search_2, "pubmed2", "", False, True)

search = pd.concat([search_1, search_2])

ft = sheets["inclusion"]
ft.columns = [
    "include",
    "authors",
    "title",
    "A",
    "B",
    "C",
    "D",
    "link",
    "pubmed2",
    "E",
    "F",
    "G",
    "H",
    "pubmed1",
]
ft = utils.extract_pmid(ft, "pubmed1")
ft = utils.extract_pmid(ft, "pubmed2")
ft = utils.extract_doi(ft, "link", "", "&")

df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Hamaker_2022", df)
