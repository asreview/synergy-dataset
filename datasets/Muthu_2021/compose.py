import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

df = pd.read_csv("https://osf.io/download/v3qjd/", sep="\t", encoding="windows-1252")

df = utils.extract_doi(df, "Url", "https://doi.org/")
df = utils.extract_pmid(df, "Url", "https://www.ncbi.nlm.nih.gov/pubmed/")
df = utils.rename_columns(
    df,
    title="Title",
    year="Publication Year",
    ft_label="Label",
)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Muthu_2021", df)
