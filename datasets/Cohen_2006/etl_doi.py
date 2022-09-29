import pandas as pd

import requests

# file_location = "https://dmice.ohsu.edu/cohenaa/epc-ir-data/epc-ir.clean.tsv"
file_location = "epc-ir.clean.tsv"

df = pd.read_table(file_location, names=["disease", "endnoteID", "pubmedID", "abstractLabel", "articleLabel"]).head(10)
df["pubmedID"] = df["pubmedID"].astype(str)
df["label_included"] = (df["articleLabel"] == "I").astype(int)

def pmid_doi(pmid):

	api = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={pmid}&retmode=json"

	try:
		r = requests.get(api)
		print(r.url, r.status_code)
		return filter(lambda d: d['idtype'] == "doi", r.json()['result'][str(pmid)]['articleids']).__next__()["value"]
	except Exception as err:
		return None

# get the DOIs
df["id"] = df["pubmedID"].map(pmid_doi)
df["id_type"] = "doi"

# save results to file
for disease in df["disease"].unique():
	df[df["disease"] == disease][["id", "id_type", "label_included"]].to_csv(f"{disease}.csv", index=False)


