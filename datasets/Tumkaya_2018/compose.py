import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
utils.unzip(
    "https://zenodo.org/records/1307117/files/DatabaseSearch_SystematicReview.zip?download=1"
)

pubmed_sheets = pd.read_excel(
    "DatabasesSearch_SystematicReview/SystematicReview_PubMed.xlsx",
    engine="openpyxl",
    sheet_name=None,
)
embase_sheets = pd.read_excel(
    "DatabasesSearch_SystematicReview/SystematicReview_Embase.xlsx",
    engine="openpyxl",
    sheet_name=None,
)

search_pm = pubmed_sheets["TitleScreen"]
search_em = embase_sheets["TitleScreenUpdated"]
search = pd.concat([search_pm, search_em])
search = utils.rename_columns(search, title="Title")
search = utils.extract_pmid(search, "Identifiers")

tiab_pm = pubmed_sheets["FullTextScreenUpdate"]
tiab_em = embase_sheets["FullTextScreenUpdate"]
tiab = pd.concat([tiab_pm, tiab_em])
tiab = utils.rename_columns(tiab, title="Title")
tiab = utils.extract_pmid(tiab, "Identifiers")

ft_pm = pubmed_sheets["MethodologyScreenUpdate"]
ft_em = embase_sheets["MethodologyScreen"]
ft = pd.concat([ft_pm, ft_em])
ft = utils.rename_columns(ft, title="Title")
ft = utils.extract_pmid(ft, "Identifiers")


df = utils.combine_datafiles(search, ft, tiab)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Tumkaya_2018", df)
