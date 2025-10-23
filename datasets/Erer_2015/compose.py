import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
df = pd.read_excel("https://osf.io/download/gwzue/")

df = utils.rename_columns(df, year="Year")
df = utils.extract_doi(df, "doi", "", "", True)
df = df.sort_values(by=['label_included'], ascending=False)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Erer_2015", df)
