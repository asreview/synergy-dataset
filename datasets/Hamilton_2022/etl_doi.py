import pandas as pd
import re

# set file location
file_location = "https://osf.io/download/4swnr/"

# identify the used columns
usecols=["title", "abstract", "issn", "notes"]

# load the data from osf
df = pd.read_csv(file_location, usecols=usecols)

# notes to label
regex = r'(?<=RAYYAN-INCLUSION: {)[a-zA-Z"=>, .]+'
df["full_labels"] = [re.search(regex, note).group() for note in df.notes]
df["label"] = [1 if "Included" in note else 0 for note in df.full_labels]

# save results to file
df[["title", "abstract", "label"]].to_csv("Hamilton_2022.csv", index=False)
