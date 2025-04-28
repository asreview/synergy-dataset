import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# get data
df_in = pd.read_excel(
    "https://zenodo.org/records/10468688/files/MiFAS_Review_Supplementary_Data.xlsx?download=1"
)

df_in = utils.rename_columns(df_in, title="Title", year="Year")
df_in = utils.extract_doi(df_in, "DOI")

ft = df_in.iloc[0:80, :]
search = df_in.iloc[80:, :]

df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Low_2023", df)
