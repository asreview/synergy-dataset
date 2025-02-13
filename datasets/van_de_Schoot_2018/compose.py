from asreview import ASReviewData
import sys

sys.path.append("../../scripts")
import utils

# Load the RIS files into ASReviewData objects
asr_inclusions = ASReviewData.from_file("https://osf.io/fg93a/download").df
asr_abstract = ASReviewData.from_file("https://osf.io/s7qf6/download").df
asr_search = ASReviewData.from_file("https://osf.io/uvr8j/download").df

# Set the labels for each dataset and merge them into a single dataframe
df = utils.combine_datafiles(asr_search, asr_inclusions, asr_abstract)
df = utils.extract_doi(df, "doi", "", "", True)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("van_de_Schoot_2018", df)
