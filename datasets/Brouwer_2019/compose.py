import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
df = pd.read_excel("https://osf.io/download/2mwkd/")

# Process data
df = utils.extract_doi(df, "doi", "", "", True)
df = utils.rename_columns(df, ft_label="included")
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Brouwer_2019", df)
