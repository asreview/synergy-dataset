import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
search = pd.read_excel("https://zenodo.org/records/7973865/files/02_Identificacion-1.2.xlsx?download=1")
tiab = pd.read_excel("https://zenodo.org/records/7973865/files/04_Screening-2.1%20sought%20for%20retrieval%20and%20excluded.xlsx?download=1")
ft = pd.read_excel("https://zenodo.org/records/7973865/files/06_Included%203.1.xlsx?download=1")

df = utils.combine_datafiles(search, ft, tiab)

df = utils.extract_doi(df, "DOI/URL")
df = utils.extract_doi(df, "DOI")
df = utils.rename_columns(df, title="Title", year="Year")

df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Sanchez-Acedo_2023", df)
