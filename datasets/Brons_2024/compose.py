import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Load the data
df = pd.read_excel("https://osf.io/9am46/download")

# Process data
df.rename(columns={"Title": "title"}, inplace=True)
df = utils.extract_doi(df, "Doi")
df = utils.extract_labels(df, ft_col="Reason", ft_value="Included")
df["label_abstract_included"] = 0
df.loc[df["Reason"] != "Abstract", "label_abstract_included"] = 1
df = df.drop(columns=["Unnamed: 0", "Reason"])
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Brons_2024", df)
