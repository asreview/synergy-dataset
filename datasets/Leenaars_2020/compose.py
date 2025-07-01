from asreview.data import RISReader
import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# load RIS files into ASReviewData object
df_pubmed = RISReader.read_data("https://osf.io/download/435yd/")
df_embase = RISReader.read_data("https://osf.io/download/q2bca/")
ft = pd.read_excel("https://osf.io/download/r94qm/", sheet_name="FT_included")[
    ["title"]
]

df_pubmed = utils.extract_pmid(df_pubmed, "accession_number")
df_embase = utils.extract_doi(df_embase, "urls", "doi\/", "&")
df_embase = utils.extract_pmid(df_embase, "urls", "pmid\/")

# set labels and turn into single dataframe
search = pd.concat([df_pubmed, df_embase], ignore_index=True)

ft["label_included"] = 1
df = search.merge(ft, on="title", how="left")
df.loc[df["label_included"].isnull(), "label_included"] = 0

df = utils.extract_doi(df, "doi", "", "&", True)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Leenaars_2020", df)
