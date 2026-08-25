import pandas as pd

import sys

sys.path.append("../../scripts")
import utils

# Get input data
df = pd.read_excel("https://osf.io/wpyrg/download")
additional_data = pd.read_excel("https://osf.io/84te6/download")
df = df.merge(
    additional_data[
        ["record_id", "doi", "accession_number", "abstract", "issn", "url"]
    ],
    how="left",
    on="record_id",
)

# Process data
df = utils.extract_doi(df, "doi", "", "", True)

df = utils.extract_pmid(df, "accession_number", "", False, True)
df = utils.extract_pmid(df, "url", "https://www.ncbi.nlm.nih.gov/pubmed/")
df = utils.extract_labels(
    df, "Include in Quality appraisal", "Include", "Exclusion reason 1", "Include"
)

df.sort_values(
    by=["label_included", "label_abstract_included"], ascending=False, inplace=True
)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Boersma-van_Dam_2024", df)
