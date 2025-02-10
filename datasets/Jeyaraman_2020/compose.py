import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
df = pd.read_csv(
    "https://osf.io/download/pkc3g/", sep="\t", encoding="windows-1252", engine="python"
)

# Process data
df = utils.rename_columns(df, title="Title", ft_label="Label")
df = utils.extract_doi(df, "DOI")
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Jeyaraman_2020", df)
