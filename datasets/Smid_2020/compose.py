import pandas as pd

# Set a key to identify the dataset
key = "Smid_2020"

# Load the dataset from an online source
df = pd.read_csv("https://osf.io/download/gxams/")

# Extract the DOI from the "doi" column and prepend "https://doi.org/"
df["doi"] = "https://doi.org/" + df["doi"].str.extract(r"(10.\S+)")

# Rename the "included" column to "label_included"
df.rename({"included": "label_included"}, axis=1, inplace=True)

# Export the raw dataset to a CSV file with the key in the filename
df.to_csv(f"{key}_raw.csv", index=False)

# Create a new dataframe with only the "doi" and "label_included" columns
df_new = df[["doi", "label_included"]].copy()

# Add an "openalex_id" column to the new dataframe
df_new["openalex_id"] = None

# Export the new dataframe with the "doi", "openalex_id", and "label_included"
# columns to a CSV file with the key in the filename
df_new[["doi", "openalex_id", "label_included"]].to_csv(f"{key}_ids.csv", index=False)
