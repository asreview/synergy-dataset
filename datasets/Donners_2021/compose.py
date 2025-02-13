from asreview import ASReviewData
import sys

sys.path.append("../../scripts")
import utils

# Read input
ft = ASReviewData.from_file("https://osf.io/download/j8stn/").df
search = ASReviewData.from_file("https://osf.io/download/zf95a/").df

df = utils.combine_datafiles(search, ft)

# Process data
df = utils.extract_doi(df, "doi", "", "", True)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Donners_2021", df)
