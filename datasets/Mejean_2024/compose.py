import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
sheets = pd.read_excel(
    "https://zenodo.org/records/10894327/files/MEJEAN_et_al_DATA_ERL.xlsx?download=1",
    engine="openpyxl",
    sheet_name=None,
)

search = sheets["5.  4 minus non peer-reviewed"]
search = utils.rename_columns(search, doi="DOI", title="Title", year="Year")
tiab = sheets["8. abstrackr relevant papers"]
ft = sheets["10. final list of papers"]


df = utils.combine_datafiles(search, ft, tiab)
df = utils.extract_doi(df, "doi", "", "", True)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Mejean_2024", df)
