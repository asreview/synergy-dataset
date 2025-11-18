import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
df = pd.read_excel("https://osf.io/download/rp2mg/")

df = utils.rename_columns(df, abstract="abstract ")
df = utils.extract_doi(df, "doi", "", "", True)
df = utils.extract_pmid(df, "PMID")
df = df.sort_values(by=['label_included'], ascending=False)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Farisogullari_2023", df)
