from asreview.data import RISReader
import sys

sys.path.append("../../scripts")
import utils

# Read input
ft = RISReader.read_data("https://osf.io/kyh7e/download")
search = RISReader.read_data("https://osf.io/t397h/download")

df = utils.combine_datafiles(search, ft)

# Process data
df = utils.extract_doi(df, "doi", "", "", True)
df = utils.extract_pmid(df, "accession_number", "", False, True)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Bos_2018", df)
