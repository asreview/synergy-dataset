import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
df = pd.read_csv(
    "https://zenodo.org/record/1162952/files/Radjenovic.csv",
    encoding="iso-8859-1",
)

df = utils.rename_columns(df, title="Document Title", year="Year")
df = utils.extract_labels(df, "label", "yes")

# Write output
utils.write_ids_files("Radjenovic_2013", df)
