import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
utils.unzip(
    "https://zenodo.org/records/7899996/files/Replication%20Package%20Review%202023.zip?download=1"
)
df = pd.read_excel(
    "Replication Package Review 3 2023/Literature Search Data/Refinement_Steps_MasterSheet.xlsx"
)

# Process data
df = utils.extract_doi(df, "DOI")
df = utils.extract_doi(df, "ArticleURL")
df = utils.rename_columns(df, title="Title", year="Year")

ft = "Refinement Step 4\n(Apply Inclusion and Exclusion criteria using the Title, Abstract, Conclusion, Full Text)"
tiab = "Refinement Step 3\nApply Inclusion and Exclusion criteria using the Title, Abstract, and Conclusion"
df = utils.extract_labels(df, ft, "Included", tiab, "Included")

df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Abgaz_2023", df)
