import pandas as pd
from asreview import ASReviewData

# load RIS from OSF into ASReviewData object
asr_inclusions = ASReviewData.from_file("https://osf.io/download/642gv/")
asr_search = ASReviewData.from_file("https://osf.io/download/tnvsw/")

# set labels and turn into single dataframe
asr_inclusions.df['label_included'] = 1
asr_search.df['label_included'] = 0
df = pd.concat([asr_inclusions.df, asr_search.df], ignore_index=True)

# adjust columns and drop missing and duplicate ids
df['doi'] = df['doi'].str.extract(r"(10.\S+)")
df['id_type'] = 'doi'
df = df.dropna(subset=['doi'])
df = df.drop_duplicates(subset=['doi'])
df['id'] = df['doi']

# save results to file
df.to_csv("Meijboom_2022_ids.csv", columns=['id', 'id_type', 'label_included'], index=False)
