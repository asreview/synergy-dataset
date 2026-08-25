import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
utils.unzip(
    "https://zenodo.org/records/4452046/files/AdaptationEnergyReviewDB.zip?download=1",
    "AdaptationEnergyReviewDB/Windows/articles.csv",
)

df = pd.read_csv("AdaptationEnergyReviewDB/Windows/articles.csv")

df = utils.extract_doi(df, "doi", "", "", True)
df = utils.extract_labels(
    df, "final_status", "inclusion", "final_status", "fulltext_exclusion"
)
df.loc[df["label_included"] == 1, "label_abstract_included"] = 1

# Write output
utils.write_ids_files("Viguie_2020", df)
