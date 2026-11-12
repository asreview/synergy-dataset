import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
df = pd.read_excel(
    "data/IMPROVE_all_screening_labels_2019_2024.xlsx"
)

df = df[df["dup#"] == 1]
df = utils.extract_labels(df, "Final inclusion\nOn_Br", 1, "Allocated \nOn_Bre", 1)
df = utils.extract_doi(df, "doi", "", "", True)
df = df.sort_values(by=['label_included'], ascending=False)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Monschau_2025", df)
