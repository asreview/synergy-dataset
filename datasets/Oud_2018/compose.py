from asreview import ASReviewData
import sys

sys.path.append("../../scripts")
import utils

# load RIS into ASReviewData object
df = ASReviewData.from_file(
    "https://osf.io/download/7shuv/?view_only=f30f6eb898e24a6f8a19734e8b1fc19b"
).df

df = utils.extract_doi(df, "doi", "", "", True)
df = utils.rename_columns(df, ft_label="included")
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Oud_2018", df)
