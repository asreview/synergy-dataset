import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Load the dataset from an online source
df = pd.read_csv("https://osf.io/download/gxams/")

# Extract the DOI from the "doi" column and prepend "https://doi.org/"
df = utils.extract_doi(df, "doi", "", "", True)
df = utils.extract_doi(df, "url", "http://link.springer.com/article/", "&")
df = utils.extract_pmid(df, "url", "http://www.ncbi.nlm.nih.gov/pmc/articles/PMC")
df = utils.rename_columns(df, ft_label="included")
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Smid_2019", df)
