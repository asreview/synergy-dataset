from asreview import ASReviewData
import sys

sys.path.append("../../scripts")
import utils

# load RIS from OSF into ASReviewData object
ft = ASReviewData.from_file("https://osf.io/download/642gv/").df
search = ASReviewData.from_file("https://osf.io/download/tnvsw/").df

df = utils.combine_datafiles(search, ft)
df = utils.extract_doi(df, "doi", "", "", True)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Meijboom_2021", df)
