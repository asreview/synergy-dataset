import re
from asreview import ASReviewData


dataset = "https://osf.io/download/gmjcv/"

asr_dataset = ASReviewData.from_file(dataset)

n_records = len(asr_dataset.df)

asr_dataset.df['id_type'] = 'doi'
asr_dataset.df['label_included'] = asr_dataset.df['Included_fulltext']
asr_dataset.df = asr_dataset.df[asr_dataset.df['DOI'].notna()]
asr_dataset.df['id'] = asr_dataset.df['DOI']

# Percentage PIDs before deduplication
print("Percentage of records with PID specified: ", len(asr_dataset.df)/n_records)

# Clean DOIs
for index, row in asr_dataset.df.iterrows():
    # Match '10.' followed by atleast 1 non whitespace characters, till first whitespace
    p = re.compile("(10.\S+)")
    result = p.search(row['id'])
    asr_dataset.df.at[index, 'id'] = result.group(1)

asr_dataset.df = asr_dataset.df.reindex(columns=['id', 'id_type', 'label_included'])

# save results to file
asr_dataset.df.to_csv("Valk_2021_ids.csv", index=False)
