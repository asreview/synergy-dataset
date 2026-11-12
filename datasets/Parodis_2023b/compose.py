import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
df = pd.read_excel("https://osf.io/download/myzdq/")

df = df[df["ssc_flag"] == 1]
df = utils.extract_doi(df, "url", "http://dx.doi.org/")
df = df.sort_values(by=['label_included'], ascending=False)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Parodis_2023b", df)
