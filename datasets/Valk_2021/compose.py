import pandas as pd

key = "Valk_2021"

# Load the dataset from an online source
df = pd.read_excel("https://osf.io/download/gmjcv/")

# Extract the DOI from the "DOI" column and prepend "https://doi.org/"
df["DOI"] = "https://doi.org/" + df["DOI"].str.extract(r"(10.\S+)")

# Rename the "Included_fulltext" and "DOI" columns
df.rename({"Included_fulltext": "label_included", "DOI": "doi"}, axis=1, inplace=True)

# Export the raw dataset
df.to_csv(f"{key}_raw.csv", index=False)

# Create a new dataframe with only the "doi" and "label_included" columns
df_new = df[["doi", "label_included"]].copy()

# Add an "openalex_id" column to the new dataframe
df_new["openalex_id"] = None

# Export the new dataframe with the "doi", "openalex_id", and "label_included"
# columns
df_new[["doi", "openalex_id", "label_included"]].to_csv(f"{key}_ids.csv", index=False)
