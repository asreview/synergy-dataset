from asreview import ASReviewData
import sys

sys.path.append("../../scripts")
import utils

# load RIS into ASReviewData object
ft = ASReviewData.from_file("https://osf.io/hy8qe/download").df
search = ASReviewData.from_file("https://osf.io/a26sz/download").df

df = utils.combine_datafiles(search, ft)

df["urls"] = df["urls"].astype("string")
df["urls"] = df["urls"].mask(
    df["urls"].notnull(), df["urls"].str.split("', '").str.join(";")
)

df = utils.extract_doi(df, "doi", "", "", True)
df = utils.extract_doi(df, "urls", "", "'")
df = utils.extract_pmid(df, "accession_number", "", False, True)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Wolters_2018", df)
