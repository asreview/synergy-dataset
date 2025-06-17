import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
search = pd.read_csv("https://zenodo.org/records/7514251/files/2.%20Unfiltered%20list.csv?download=1")
ft = pd.read_csv("https://zenodo.org/records/7514251/files/3.%20Selected%20List.csv?download=1", skiprows=1)

search = utils.rename_columns(search, title="Title", year="Year")
ft = utils.rename_columns(ft, title="Title", year="Year")
ft = utils.extract_doi(ft, "DOI")

df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Greca_2023", df)
