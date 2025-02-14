import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Get input data
df = pd.read_excel("https://osf.io/sjzr5/download", sheet_name="Sheet1")

df = utils.extract_doi(df, "Link")
df = utils.rename_columns(df, title="Title", year="Year")

# Rename long column name and get labels 
df = df.rename(
    columns={
        "Full codes (0=excluded based on the title; 1.1= Reviews/ editorials/ commentaries/ protocols/ theoretical studies; 1.2= No assessment of attachment or suicide; 1.3= Qualitative research; 1.4= Population < 18 yo; 2.1= Reviews/ editorials/ commentaries/ protocols/ theoretical studies; 2.2= No assessment of attachment or suicide; 2.3= Qualitative research; 2.4= Population < 18 y; 2.5= No validated measure of adult attachment style; 3=elegible)": "label"
    }
)
df = df[df.label != "DUPLICADO"]
df["label"] = df["label"].astype(float)
df["label_included"] = (df["label"] == 3).astype(int)
df["label_abstract_included"] = (df["label"] >= 2).astype(int)

df.sort_values(
    by=["label_included", "label_abstract_included"], ascending=False, inplace=True
)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Maciel_2024", df)
