import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
df = pd.read_csv(
    "https://zenodo.org/records/10423427/files/citation_screening_deduplicated_corpus.csv?download=1",
    sep="\t",
    names=["title", "PMID", "abstract", "inclusion", "keywords"],
)

df = utils.extract_pmid(df, "PMID")
df = utils.extract_labels(df, "inclusion", "include")

# Write output
utils.write_ids_files("Hilfiker_2017", df)
