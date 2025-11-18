import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

sheets_blood = pd.read_excel(
    "data/1-s2.0-S2666571922000214-mmc1.xlsx",
    engine="openpyxl",
    sheet_name=None,
)
sheets_urine = pd.read_excel(
    "data/1-s2.0-S2666571922000214-mmc2.xlsx",
    engine="openpyxl",
    sheet_name=None,
)

search_blood = sheets_blood["Duplicates removed"]
search_urine = sheets_urine["Duplicates removed"]
search = pd.concat([search_blood, search_urine])
search = utils.rename_columns(search, title="Title", year="Publication Year", authors="Authors")
search = utils.extract_doi(search, "DOI")
search = utils.extract_pmid(search, "PMID")

tiab_blood = sheets_blood["Accepted based on abstract"]
tiab_urine = sheets_urine["Eligible based on abstract"]
tiab = pd.concat([tiab_blood, tiab_urine])
tiab = utils.rename_columns(tiab, title="Title", year="Publication Year", authors="Authors")
tiab = utils.extract_doi(tiab, "DOI")
tiab = utils.extract_pmid(tiab, "PMID")

ft_blood = sheets_blood["Final inclusion"]
ft_urine = sheets_urine["Eligible for analysis"]
ft = pd.concat([ft_blood, ft_urine])
ft = utils.rename_columns(ft, title="Title", year="Publication Year", authors="Authors")
ft = utils.extract_doi(ft, "DOI")
ft = utils.extract_pmid(ft, "PMID")

df = utils.combine_datafiles(search, ft, tiab)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Dolinska_2022", df)
