import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
df = pd.read_excel(
    "https://osf.io/download/jpc7m/"
)

# The review contains inclusions from another review. Remove those:
df = df[(df["label_included"] == 0) | df.index.isin([i for i in range(3745)])]

df = utils.extract_doi(df, "doi", "", "", True)
df = df.sort_values(by=['label_included'], ascending=False)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Sepriano_2020", df)
