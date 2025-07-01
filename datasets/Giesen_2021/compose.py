from asreview.data import RISReader, CSVReader
import sys

sys.path.append("../../scripts")
import utils

# Read input
utils.unzip("https://osf.io/6nwg7/download", "articles.ris", "search.ris")
utils.unzip("https://osf.io/vchfj/download", "articles.ris", "ti_ab.ris")

search = RISReader.read_data("search.ris")
ti_ab = RISReader.read_data("ti_ab.ris")

ft = CSVReader.read_data("https://osf.io/5djeu/download")

df = utils.combine_datafiles(search, ft, ti_ab)

# Process data
df = utils.extract_doi(df, "urls" "", "&")
df = utils.extract_year(df, "publication_year")
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Giesen_2021", df)
