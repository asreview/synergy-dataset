import pandas as pd
import sys
sys.path.append("../../scripts")
import utils

# Read input
df = pd.read_csv("https://zenodo.org/record/1162952/files/Hall.csv")

df = utils.extract_labels(df, "label", "yes")

# Write output
utils.write_ids_files("Hall_2011", df)
