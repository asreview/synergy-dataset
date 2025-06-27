from asreview import data
import sys

sys.path.append("../../scripts")
import utils

# load RIS into ASReviewData object
ft = data.RISReader.read_data(
    "https://zenodo.org/record/3625931/files/DOKU_All%20Included_20200116_cap.txt"
)
ti_ab = data.RISReader.read_data(
    "https://zenodo.org/record/3625931/files/DOKU_All%20FT-Screening_20200116_cap.txt"
)
search = data.RISReader.read_data(
    "https://zenodo.org/record/3625931/files/DOKU_All%20TiAb-Screening_20200116_cap.txt"
)

# set labels and turn into single dataframe
df = utils.combine_datafiles(search, ft, ti_ab)

# adjust columns and drop missing and duplicate ids
df = utils.extract_doi(df, "doi", "", "", True)
df = utils.extract_pmid(df, "urls", r"id\=pmid\:")
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Appenzeller-Herzog_2019", df)
