import pandas as pd
from asreview import ASReviewData

# load RIS from OSF into ASReviewData objects
asr_inclusions_1 = ASReviewData.from_file("https://osf.io/download/pa6zn/")
asr_inclusions_2 = ASReviewData.from_file("https://osf.io/download/96xq5/")
asr_search_1 = ASReviewData.from_file("https://osf.io/download/9rj5y/")
asr_search_2 = ASReviewData.from_file("https://osf.io/download/pr2es/")

# set labels and turn into single dataframe
asr_inclusions_1.df['label_included'] = 1
asr_inclusions_2.df['label_included'] = 1
asr_search_1.df['label_included'] = 0
asr_search_2.df['label_included'] = 0
df = pd.concat([asr_inclusions_1.df, asr_inclusions_2.df,
                asr_search_1.df, asr_search_2.df], ignore_index=True)

# adjust columns and drop missing and duplicate ids
df['doi'] = df['doi'].str.extract(r"(10.\S+)")
df['id_type'] = 'doi'
df = df.dropna(subset=['doi'])
df = df.drop_duplicates(subset=['doi'])
df['id'] = df['doi']

# save results to file
df.to_csv("Berk_2021_ids.csv", columns=['id', 'id_type', 'label_included'], index=False)
