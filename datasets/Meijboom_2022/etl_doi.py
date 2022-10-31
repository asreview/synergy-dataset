import re
import numpy as np
import pandas as pd
from asreview import ASReviewData


file_search = "https://osf.io/download/tnvsw/"
file_inclusions = "https://osf.io/download/642gv/"

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
ids = df_output.index.to_list()
df_output = df_output.reset_index()
df_output['id_type'] = "doi"
df_output['id'] = ids
df_output = df_output.reindex(columns=['id', 'id_type', 'label_included'])

# Clean DOIs
for index, row in df_output.iterrows():
    # Match '10.' followed by atleast 1 non whitespace characters, till first whitespace
    p = re.compile("(10.\S+)")
    result = p.search(row['id'])
    df_output.at[index, 'id'] = result.group(1)

# save results to file
df_output.to_csv("Meijboom_2022_ids.csv", index=False)