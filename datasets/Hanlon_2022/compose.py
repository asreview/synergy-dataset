import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
df = pd.read_excel(
    "https://zenodo.org/records/6966157/files/Abstract_screening_RA_frailty_full_texts.xlsx?download=1"
)

# process data
df = utils.rename_columns(df, title="Title", year="Year")
df = utils.extract_labels(df, "full_text_screen", "y", "Abstract_screen", "y")

df.sort_values(
    by=["label_included", "label_abstract_included"], ascending=False, inplace=True
)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Hanlon_2022", df)
