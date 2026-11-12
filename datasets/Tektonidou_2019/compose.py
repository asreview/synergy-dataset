import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
df = pd.read_excel("https://osf.io/download/p8nzk/")

df = utils.rename_columns(df, year="Year", authors="author")
df = utils.extract_doi(df, "doi", "", "", True)
df = df.sort_values(by=['label_included'], ascending=False)
df = utils.drop_duplicates(df)

# Drop one duplicate that we know of in the dataset
df = df[df["doi"] != "https://doi.org/10.1097/01.ogx.0000172317.50128.ed"]

# Write output
utils.write_ids_files("Tektonidou_2019", df)
