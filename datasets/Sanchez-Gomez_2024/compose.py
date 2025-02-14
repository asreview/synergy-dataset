from asreview import ASReviewData
import sys

sys.path.append("../../scripts")
import utils

# Data comes from: https://osf.io/tg56j/
search = ASReviewData.from_file("https://osf.io/uvf9q/download").df
ti_ab = ASReviewData.from_file("https://osf.io/35m6h/download").df
ft = ASReviewData.from_file("https://osf.io/z4tpn/download").df

df = utils.combine_datafiles(search, ft, ti_ab)
df = utils.extract_doi(df, "doi", "", "", True)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Sanchez-Gomez_2024", df)
