from asreview.data import RISReader
import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Original data that was recreened
# https://doi.org/10.34894/YXR1X3
df_relabeled = pd.read_excel("data/PTSS_Data_Synergy-corrected.xlsx")
df_relabeled = utils.extract_doi(df_relabeled, "doi", "", "", True)
df_relabeled = utils.rename_columns(
    df_relabeled, ft_label="FT-corrected", ti_ab_label="TI-AB-corrected"
)

# Add new entries from hunt for the last relevant paper
#  https://doi.org/10.34894/CRE6ZC
df_update = pd.read_excel("data/PTSS_Data_Foras_2025-02-05.xlsx")
df_update = utils.extract_doi(df_update, "doi", "", "", True)
df_update = utils.rename_columns(
    df_update, ft_label="label_included_FT", ti_ab_label="label_included_TIAB"
)
df_update = df_update[df_update["filter_duplicate"] != 1]

df = pd.concat([df_relabeled, df_update])
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("van_de_Schoot_2025", df)
