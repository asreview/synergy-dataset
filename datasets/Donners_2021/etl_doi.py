import numpy as np
import pandas as pd
from asreview import ASReviewData


file_search = "https://osf.io/download/zf95a/"
file_inclusions = "https://osf.io/download/j8stn/"

asr_search = ASReviewData.from_file(file_search)
asr_inclusions = ASReviewData.from_file(file_inclusions)

n_records = len(asr_search.df)

asr_search.df['id_type'] = "doi"
asr_search.df['label_included'] = 0

asr_search.df = asr_search.df[asr_search.df['doi'].notna()]

# Percentage PIDs before deduplication
print("Percentage of records with PID specified: ", len(asr_search.df)/n_records)

dict_doi = asr_search.df.set_index('doi')['label_included'].to_dict()

# Set label_included to 1 for inclusions
for inclusion_doi in asr_inclusions.df['doi']:
    if inclusion_doi is not np.nan:
        dict_doi[inclusion_doi] = 1

# Convert dict to dataframe and reorder columns
df_output = pd.DataFrame.from_dict(dict_doi, orient='index', columns=['label_included'])
df_output['id_type'] = "doi"
df_output = df_output.reindex(columns=['id_type', 'label_included'])

# save results to file
df_output.to_csv("Donners_2021_ids.csv", index_label="id")
