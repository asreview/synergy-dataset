import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
df = pd.read_excel(
    "https://osf.io/download/68d69c0d35629c9a90d4eb6d/"
)

df = utils.rename_columns(df, abstract="abstract ")
df = utils.extract_doi(df, "doi", "", "", True)
df = df.sort_values(by=['label_included'], ascending=False)
df = utils.drop_duplicates(df)


# Insert openalex_id for the specific DOI and replace DOI with the correct one (poster vs article that was actually cited)
df["openalex_id"] = df["openalex_id"].astype("string")
mask = df["doi"].str.contains(
    "10.1136/annrheumdis-2022-eular.803", na=False
)

df.loc[mask, ["doi", "openalex_id"]] = [
    "https://doi.org/10.1136/ard-2022-223739",
    "https://openalex.org/W4362460104"
]



# Write output
utils.write_ids_files("Bindoli_2024b", df)
