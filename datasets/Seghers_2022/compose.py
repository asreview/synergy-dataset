import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
sheets = pd.read_excel(
    "https://zenodo.org/records/7194756/files/zenodo-search-and%20output-Patient%20Preferences%20for%20Treatment%20Outcomes%20in%20Oncology%20with%20a%20focus%20on%20the%20older%20patient.xlsx?download=1",
    engine="openpyxl",
    sheet_name=None,
    header=None,
)

# Note: inclusions have no headers, search does

search = sheets["output search"].iloc[1:, :].copy()

search.columns = [
    "title",
    "A",
    "B",
    "C",
    "D",
    "E",
    "pubmed",
    "link",
    "link2",
    "link3",
    "link4",
    "link5",
    "link6",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
]
search["pubmed"] = search["pubmed"].astype("string")
search = utils.extract_pmid(search, "pubmed", "", False, True)
search = utils.extract_doi(search, "link", "", "&")
search = utils.extract_doi(search, "link2", "", "&")
search = utils.extract_doi(search, "link3", "", "&")
search = utils.extract_doi(search, "link4", "", "&")
search = utils.extract_doi(search, "link5", "", "&")
search = utils.extract_doi(search, "link6", "", "&")

ft = sheets["included studies"]
ft.columns = ["authors", "title", "A", "B", "C", "pubmed", "link"]
ft["pubmed"] = ft["pubmed"].astype("string")
ft = utils.extract_pmid(ft, "pubmed", "", False, True)
ft = utils.extract_doi(ft, "link", "", "&")

df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Seghers_2022", df)
