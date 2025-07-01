from asreview.data import RISReader

import sys

sys.path.append("../../scripts")
import utils

# Get input data
search = RISReader.read_data(
    "https://zenodo.org/records/13957522/files/Initial%20search%20(outreach%20included).ris"
)
ti_ab_exclude = RISReader.read_data(
    "https://zenodo.org/records/13957522/files/Excluded%20first%20round.ris"
)
ti_ab = search[
    ~search["primary_title"].isin(ti_ab_exclude["primary_title"])
].reset_index(drop=True)
ft = RISReader.read_data(
    "https://zenodo.org/records/13957522/files/Included%20papers.ris"
)

df = utils.combine_datafiles(search, ft, ti_ab)

# Process data
df = utils.extract_doi(df, "doi", "", "", True)
df = utils.extract_year(df, "publication_year")
df = utils.rename_columns(df, title="primary_title")
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Wijnen_2024", df)
