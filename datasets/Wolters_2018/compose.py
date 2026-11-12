from asreview.data import RISReader
import sys

sys.path.append("../../scripts")
import utils

# load RIS into ASReviewData object
ft = RISReader.read_data("https://osf.io/hy8qe/download")
search = RISReader.read_data("https://osf.io/a26sz/download")

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
