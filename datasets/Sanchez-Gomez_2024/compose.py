from asreview.data import RISReader
import sys

sys.path.append("../../scripts")
import utils

# Data comes from: https://osf.io/tg56j/
search = RISReader.read_data("https://osf.io/uvf9q/download")
ti_ab = RISReader.read_data("https://osf.io/35m6h/download")
ft = RISReader.read_data("https://osf.io/z4tpn/download")

df = utils.combine_datafiles(search, ft, ti_ab)
df = utils.extract_doi(df, "doi", "", "", True)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Sanchez-Gomez_2024", df)
