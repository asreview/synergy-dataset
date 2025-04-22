import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
search = pd.read_excel("https://zenodo.org/records/4280896/files/all_sources_noCOLLECTIONS_DUPLICATES.xlsx?download=1")
search = utils.extract_doi(search, "DOI")
search = utils.rename_columns(search, title="Title", year="Year")

ft_input = pd.read_excel("https://zenodo.org/records/4280896/files/Primary%20studies_after%20QA.xlsx?download=1")
ft_1 = ft_input.iloc[:27, :]
ft_2 = ft_input.iloc[27:31, :]
ft_3 = ft_input.iloc[31:65, :]

ft_1 = utils.extract_doi(ft_1, "DOI")
ft_1 = utils.rename_columns(ft_1, title="Title SCOPUS", year="Year")

ft_2 = utils.rename_columns(ft_2, title="Authors", year="Year")

ft_3 = utils.extract_doi(ft_3, "Cited by")
ft_3 = utils.rename_columns(ft_3, title="REF", year="Unnamed: 3")

ft = pd.concat([ft_1, ft_2, ft_3])

df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Adamo_2021", df)
