import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
df = pd.read_excel("https://osf.io/download/t8cgs/")

df = df.sort_values(by=['label_included'], ascending=False)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Ramiro_2015", df)
