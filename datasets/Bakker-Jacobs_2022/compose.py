from asreview import ASReviewData
import sys

sys.path.append("../../scripts")
import utils

# Read input
utils.unzip("https://osf.io/tgv4b/download", "articles.ris", "search.ris")
utils.unzip("https://osf.io/5bmy3/download", "articles.ris", "ti_ab.ris")

search = ASReviewData.from_file("search.ris").df
ti_ab = ASReviewData.from_file("ti_ab.ris").df

ft = ASReviewData.from_file("https://osf.io/9k2xs/download").df

df = utils.combine_datafiles(search, ft, ti_ab)

# Process data
df = utils.extract_year(df, "publication_year")
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Bakker-Jacobs_2022", df)
