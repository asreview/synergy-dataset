from asreview import ASReviewData
import pandas as pd

import sys

sys.path.append("../../scripts")
import utils

# Get input files
utils.unzip("https://surfdrive.surf.nl/files/index.php/s/UcfIYP3K612w0oA/download")

search_1 = ASReviewData.from_file(
    "ASReview/search results/My EndNote Library_vanBallegooijen_20210409.txt"
).df
search_2 = pd.read_csv("ASReview/search results/update 2024 search results.csv")
col_names = [
    "type",
    "authors",
    "year",
    "title",
    "journal",
    "",
    "",
    "",
    "",
    "",
    "url",
    "doi",
    "",
    "abstract",
]
search_3 = pd.read_excel(
    "ASReview/search results/vanBallegooijen_20220506_databaseSuicidepreventie.xlsx",
    header=None,
    names=col_names,
)
search = pd.concat([search_1, search_2, search_3])

ft_exclusions = pd.read_csv("ASReview/review_63783_excluded_csv_20241003192320.csv")
ft = pd.read_csv("ASReview/full_text_inclusions.csv")
ti_ab = pd.concat([ft, ft_exclusions])

df = utils.combine_datafiles(search, ft, ti_ab)

# Process data
df = utils.extract_title(df, "Title")
df = utils.extract_year(df, "Published Year")
df = utils.extract_year(df, "Publication Year")
df = utils.extract_doi(df, "DOI")
df = utils.extract_doi(df, "doi", "", "", True)

df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("van_Ballegooijen_2024", df)
