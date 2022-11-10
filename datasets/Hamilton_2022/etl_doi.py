"""
A module for importing data from the Hamilton 2022 dataset. This module
transforms the Rayyan data into a format that is compatible with other
platforms.
"""

import pandas as pd


# set file location
file_location = "https://osf.io/download/4swnr/"

# identify the used columns
usecols = ["title", "abstract", "issn", "notes"]

# load the data from osf
df = pd.read_csv(file_location, usecols=usecols)

# notes to label
regex = r'(?<=RAYYAN-INCLUSION: ){([a-zA-Z"=>, .]+)}'
df["full_labels"] = df["full_labels"] = df["notes"].str.extract(regex)
df["label"] = [1 if "Included" in note else 0 for note in df.full_labels]

# save results to file
df[["title", "abstract", "label"]].to_csv("Hamilton_2022.csv", index=False)
