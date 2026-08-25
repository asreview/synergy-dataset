import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
df = pd.read_excel("https://osf.io/download/krngx")

df = utils.extract_doi(df, "doi", "", " \[doi\]", True)
df = utils.extract_doi(df, "url")
df = utils.extract_pmid(df, "url", "pubmed\/")
df = utils.rename_columns(df, ft_label="included")
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Pijls_2017", df)
