from asreview import ASReviewData
import sys

sys.path.append("../../scripts")
import utils

# Read input
utils.unzip("https://osf.io/6nwg7/download", "articles.ris", "data/search.ris")
utils.unzip("https://osf.io/vchfj/download", "articles.ris", "data/ti_ab.ris")

search = ASReviewData.from_file("data/search.ris").df
ti_ab = ASReviewData.from_file("data/ti_ab.ris").df

ft = ASReviewData.from_file("https://osf.io/5djeu/download").df

df = utils.combine_datafiles(search, ft, ti_ab)

# Process data
df = utils.extract_doi(df, "url" "", "&")
df = utils.extract_year(df, "publication_year")
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Giesen_2021", df)
