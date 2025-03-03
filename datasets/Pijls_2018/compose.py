import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
df = pd.read_excel("https://osf.io/u39zy/download")

df = utils.extract_pmid(df, "accession_number", "", False, True)
df = utils.extract_doi(df, "doi", "", "", True)
df = utils.rename_columns(df, ft_label="included")
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Pijls_2018", df)
