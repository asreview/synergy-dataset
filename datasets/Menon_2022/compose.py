import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

search = pd.read_csv("https://osf.io/download/y83tu/").rename(
    {"pubmed_id": "pmid"}, axis=1
)
ft = pd.read_excel("https://osf.io/download/mgxwj/").rename(
    {"DOI name": "doi", "PubMed ID": "pmid"}, axis=1
)

# set labels and turn into single dataframe
df = utils.combine_datafiles(search, ft)
df = utils.rename_columns(df, title="Title")
df = utils.extract_doi(df, "doi", "", "", True)
df = utils.extract_pmid(df, "pmid", "", True)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Menon_2022", df)
