import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
df = pd.read_excel("https://osf.io/download/3sdqu/")

df = utils.rename_columns(df, year="Year")
df = utils.extract_doi(df, "doi", "", "", True)
df = utils.extract_pmid(df, "PMID")
df = df.sort_values(by=['label_included'], ascending=False)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Marques_2021", df)
