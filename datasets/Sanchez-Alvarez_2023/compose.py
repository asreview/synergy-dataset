import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
df = pd.read_excel(
    "https://osf.io/download/t2w6h/"
)

df = utils.rename_columns(df, year="Published Year")
df = utils.extract_doi(df, "DOI")
df = df.sort_values(by=['label_included'], ascending=False)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Sanchez-Alvarez_2023", df)
