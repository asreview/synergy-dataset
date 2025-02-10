import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
df = pd.read_table(
    "https://dmice.ohsu.edu/cohenaa/epc-ir-data/epc-ir.clean.tsv",
    names=["disease", "endnoteID", "pubmed", "abstract_label", "ft_label"],
)

# Process data
df = df[df.disease == "SkeletalMuscleRelaxants"]

df = utils.extract_labels(df, "ft_label", "I", "abstract_label", "I")
df = utils.extract_pmid(df, "pubmed")
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Chou_2004", df)
