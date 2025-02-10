import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

df = pd.read_excel(
    "https://static-content.springer.com/esm/art%3A10.1186%2Fs13643-016-0263-z/MediaObjects/13643_2016_263_MOESM1_ESM.xlsx",
    sheet_name="BPA",
)
df = utils.extract_pmid(df, "PMID")
df = utils.extract_labels(df, "Status", "Included")
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Wassenaar_2017", df)
