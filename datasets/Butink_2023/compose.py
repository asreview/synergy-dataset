import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
df = pd.read_excel("https://osf.io/download/fr4u7/")

df = utils.rename_columns(df, year="Year", ti_ab_label="OPTIONALLY\nIncluded after the title/abstract phase = 1, \nExcluded after the title/abstract phase = 0")
df = utils.extract_doi(df, "doi", "", "", True)
df = df.sort_values(by=['label_included'], ascending=False)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Butink_2023", df)
