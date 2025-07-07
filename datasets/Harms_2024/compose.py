from asreview.data import RISReader
import sys

sys.path.append("../../scripts")
import utils

# Read input
search = RISReader.read_data(
    "https://zenodo.org/records/14857618/files/B_01_recordsscreened-title-keywords.ris?download=1"
)
tiab = RISReader.read_data(
    "https://zenodo.org/records/14857618/files/B_03_recordsscreened-fulltext.ris?download=1"
)
ft = RISReader.read_data(
    "https://zenodo.org/records/14857618/files/B_04_studiesincluded.ris?download=1"
)

df = utils.combine_datafiles(search, ft, tiab)
df = utils.extract_doi(df, "doi", "", "", True)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Harms_2024", df)
