import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
df = pd.read_excel(
    "https://osf.io/download/68d69c0d35629c9a90d4eb6d/"
)

df = utils.rename_columns(df, abstract="abstract ")
df = utils.extract_doi(df, "doi", "", "", True)
df = df.sort_values(by=['label_included'], ascending=False)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Bindoli_2024b", df)
