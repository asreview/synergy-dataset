from asreview.data import RISReader
import sys

sys.path.append("../../scripts")
import utils

# load RIS from OSF into ASReviewData object
ft = RISReader.read_data("https://osf.io/download/642gv/")
search = RISReader.read_data("https://osf.io/download/tnvsw/")

df = utils.combine_datafiles(search, ft)
df = utils.extract_doi(df, "doi", "", "", True)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Meijboom_2021", df)
