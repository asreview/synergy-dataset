import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

df = pd.read_csv(
    "https://zenodo.org/records/5647093/files/Initial_Screening.csv?download=1", sep=";", encoding='latin-1'
)

df = utils.extract_doi(df, "DOI")
df = utils.rename_columns(df, title="Title")
df = utils.extract_labels(df, "Final result", "Accepted", "include decision", "Y")

df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Lewowski_2021", df)
