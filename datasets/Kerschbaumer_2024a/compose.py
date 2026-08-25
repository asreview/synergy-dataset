import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
df = pd.read_excel(
    "https://osf.io/download/68d69c01dffe413948b8f843/"
)

df = utils.rename_columns(df, ft_label="final_included")
df = utils.extract_doi(df, "doi", "", "", True)
df = df.sort_values(by=['label_included'], ascending=False)
df = utils.drop_duplicates(df)

# Drop one duplicate that we know of in the dataset
df = df[df["doi"] != "https://doi.org/10.1016/S0140-6736(20)30680-2"]

# Write output
utils.write_ids_files("Kerschbaumer_2024a", df)
