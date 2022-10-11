import json
import glob
from pathlib import Path

import requests
import pandas as pd


with open("datasets/Cohen_2006/openalex/Cohen_2006_Triptans_ids_metadata_openalex.json", "r", encoding="utf-8") as f:
    res = json.load(f)


def invert_abstract(inv_index):

	if inv_index is not None:
		l = [(w, p) for w, pos in inv_index.items() for p in pos ]
		return " ".join(map(lambda x: x[0], sorted(l, key=lambda x: x[1])))

df_w = []
for w in res:

	df_w.append({
		"title":w["title"],
		"abstract": invert_abstract(w["abstract_inverted_index"]),
		"label_included": w["systematic_review"]["study_selection"]
	})

df = pd.DataFrame(df_w)

print(df)
