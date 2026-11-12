import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
df = pd.read_excel("https://osf.io/download/qyxe5/")

df = utils.rename_columns(
    df,
    year="Publication Year",
    ti_ab_label="OPTIONALLY Included after the title/abstract phase = 1,  Excluded after the title/abstract phase = 0",
    authors="author"
)
df = utils.extract_doi(df, "doi", "", "", True)
df = utils.extract_pmid(df, "PMID")
df = df.sort_values(by=["label_included"], ascending=False)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Zanframundo_2022", df)
