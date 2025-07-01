from asreview.data import RISReader
import sys

sys.path.append("../../scripts")
import utils

# Read input
utils.unzip("https://osf.io/tgv4b/download", "articles.ris", "search.ris")
utils.unzip("https://osf.io/5bmy3/download", "articles.ris", "ti_ab.ris")

search = RISReader.read_data("search.ris")
ti_ab = RISReader.read_data("ti_ab.ris")

ft = RISReader.read_data("https://osf.io/9k2xs/download")

df = utils.combine_datafiles(search, ft, ti_ab)

# Process data
df = utils.extract_year(df, "publication_year")
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Bakker-Jacobs_2022", df)
