import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Load the dataset from an online source
df = pd.read_excel("https://osf.io/download/gmjcv/")

# process data
df = utils.extract_doi(df, "DOI")
df = utils.rename_columns(
    df,
    ft_label="Included_fulltext",
    ti_ab_label="Included_abstract",
    year="Publication Year",
)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("van_der_Valk_2021", df)
