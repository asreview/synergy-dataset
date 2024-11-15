from asreview import ASReviewData
import pandas as pd
from pathlib import Path
import numpy as np

p = Path().absolute() / 'data'
p.mkdir(parents=True, exist_ok=True)

# Data comes from: https://zenodo.org/records/13957522
search = ASReviewData.from_file("https://zenodo.org/records/13957522/files/Initial%20search%20(outreach%20included).ris").df
search["year"] = search["publication_year"].str.extract(r"(\d+)")
search["title"] = search["primary_title"]
search.to_csv(p / 'search.csv')

ti_ab_exclude = ASReviewData.from_file("https://zenodo.org/records/13957522/files/Excluded%20first%20round.ris").df
ti_ab = search[~search[['primary_title']].apply(lambda x: np.in1d(x,ti_ab_exclude).all(),axis=1)].reset_index(drop=True)
ti_ab["year"] = ti_ab["publication_year"].str.extract(r"(\d+)")
ti_ab["title"] = ti_ab["primary_title"]
ti_ab.to_csv(p / 'ti_ab.csv')

ft = ASReviewData.from_file("https://zenodo.org/records/13957522/files/Included%20papers.ris").df
ft["year"] = ft["publication_year"].str.extract(r"(\d+)")
ft["title"] = ft["primary_title"]
ft.to_csv(p / 'ft.csv')
