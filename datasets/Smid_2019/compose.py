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
df = utils.rename_columns(df, ft_label="included", authors="author")
df = utils.drop_duplicates(df)

# We remove this doi, since it does not exist in the original data or paper
df = df[~df["doi"].astype(str).str.contains("10.3758/s13428-017-0870-1", na=False)]

# We add this oa_id/doi/pmid, since it is an inclusion in the original paper
ft_manual = pd.DataFrame([{"openalex_id": "https://openalex.org/w2609159880", "doi": "https://doi.org/10.1080/10705511.2017.1312407", "pmid": 29662296, "label_included": 1}])
df = pd.concat([df, ft_manual])

# Write output
utils.write_ids_files("Smid_2019", df)
