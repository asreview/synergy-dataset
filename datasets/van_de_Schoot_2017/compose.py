import pandas as pd
from asreview import ASReviewData

# Set a key to identify the data files
key = "van_de_Schoot_2017"

# Load the RIS files into ASReviewData objects
asr_inclusions = ASReviewData.from_file("https://osf.io/fg93a/download")
asr_search = ASReviewData.from_file("https://osf.io/uvr8j/download")

# Set the labels for each dataset and merge them into a single dataframe
asr_inclusions.df["label_included"] = 1
asr_search.df["label_included"] = 0
df = pd.concat([asr_inclusions.df, asr_search.df], ignore_index=True)

# Adjust the "doi" column by extracting the DOI and prepending "https://doi.org/"
df["doi"] = "https://doi.org/" + df["doi"].str.extract(r"(10.\S+)")

# Export the raw dataset
df.to_csv(f"{key}_raw.csv", index=False)

# Create a new dataframe with only the "doi" and "label_included" columns
df_new = df[["doi", "label_included"]].copy()

# Add an "openalex_id" column to the new dataframe
df_new["openalex_id"] = None

# Export the new dataframe with the "doi", "openalex_id", and "label_included"
# columns
df_new[["doi", "openalex_id", "label_included"]].to_csv(f"{key}_ids.csv", index=False)
