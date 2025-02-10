from asreview import ASReviewData
import sys

sys.path.append("../../scripts")
import utils

# Read input
ft = ASReviewData.from_file("https://osf.io/kyh7e/download").df
search = ASReviewData.from_file("https://osf.io/t397h/download").df

df = utils.combine_datafiles(search, ft)

# Process data
df = utils.extract_doi(df, "doi", "", "", True)
df = utils.extract_pmid(df, "accession_number", "", False, True)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Bos_2018", df)
