import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
df = pd.read_excel(
    "https://zenodo.org/records/7626621/files/SystematicMappingStudyLegalNLP.xlsx?download=1",
    engine="openpyxl",
    sheet_name="ResultMapping",
    skiprows=2,
)

df = df.iloc[1:487, :].copy()

df = utils.rename_columns(df, title="Title", year="Year")
df = utils.extract_doi(df, "CitesURL")
df["Accepted by full read YES/NO"] = df["Accepted by full read YES/NO"].str.lower()
df = utils.extract_labels(df, "Accepted by full read YES/NO", "yes")
df["label_abstract_included"] = df["YES / Include"].notna().astype(int)

df = df.sort_values(by=["label_included", "label_abstract_included"], ascending=False)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Quevedo_2023", df)
