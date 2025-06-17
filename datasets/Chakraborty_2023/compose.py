import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
s1 = pd.read_excel(
    "https://zenodo.org/records/7685694/files/search_s1.xlsx?download=1",
    engine="openpyxl",
    sheet_name=None,
)
s2 = pd.read_excel(
    "https://zenodo.org/records/7685694/files/search_s2.xlsx?download=1",
    engine="openpyxl",
    sheet_name=None,
)

search1 = s1["step1title_venue"]
search2 = s2["step1title_venue"]
search = pd.concat([search1, search2])

tiabft1 = s1["step3fulltext"]
tiabft2 = s2["step3fulltext"]
tiabft = pd.concat([tiabft1, tiabft2])
tiabft["label_abstract_included"] = 1
tiabft = utils.extract_labels(tiabft, "include SC", "y")

df = search.join(
    tiabft.set_index("Paper Title"), on="Title", lsuffix="_search", rsuffix="_ft"
)
df = utils.rename_columns(df, title="Title", year="Year")
df = utils.extract_labels(df, "label_included", 1, "label_abstract_included", 1)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Chakraborty_2023", df)
