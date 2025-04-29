import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# load RIS into ASReviewData object
ft = pd.read_csv("https://osf.io/vuyhq/download")
excluded_ft = pd.read_csv("https://osf.io/puwrd/download")
excluded_tiab = pd.read_csv("https://osf.io/3grcz/download")

df = utils.combine_datafiles(excluded_tiab, ft, excluded_ft)
df = utils.rename_columns(df, title="Title", year="Published Year")
df = utils.extract_doi(df, "DOI")

# fix broken DOI that break openalex/pyalex
# Emily: Check if this is still needed?
df.loc[df["doi"] == "https://doi.org/10.1002/(SICI)1097-0134(199606)25:2&lt", "doi"] = (
    "https://doi.org/10.1002/(SICI)1097-0134(199606)25:2<215::AID-PROT7>3.0.CO;2-G"
)

df = utils.extract_pmid(df, "Ref", "", False, True)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("van_Dis_2019", df)
