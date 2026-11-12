import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
df = pd.read_excel(
    "https://osf.io/download/va53e/"
)

df = utils.extract_doi(df, "doi", "", "", True)
df = utils.extract_pmid(df, "url")
df = df.sort_values(by=['label_included'], ascending=False)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Aouad_2024", df)
