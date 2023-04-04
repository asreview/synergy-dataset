import pandas as pd

url = "https://static-content.springer.com/esm/art%3A10.1186%2Fs13643-016-0263-z/MediaObjects/13643_2016_263_MOESM1_ESM.xlsx"

df_bpa = pd.read_excel(url, sheet_name="BPA")
df_bpa["label_included"] = df_bpa["Status"].replace({"Excluded": 0, "Included": 1})
df_bpa["pmid"] = "https://pubmed.ncbi.nlm.nih.gov/" + df_bpa["PMID"].astype(str)
df_bpa["doi"] = None

df_bpa.to_csv("Wassenaar_2017_raw.csv", index=False)

df_new = df_bpa[["pmid", "doi", "label_included"]].copy()
df_new["openalex_id"] = None
df_new[["pmid", "doi", "openalex_id", "label_included"]].to_csv(
    "Wassenaar_2017_ids.csv", index=False
)


df_pfos = pd.read_excel(url, sheet_name="PFOS-PFOA")
df_pfos["label_included"] = df_pfos["Status"].replace({"Excluded": 0, "Included": 1})
df_pfos["doi"] = None
df_pfos["pmid"] = "https://pubmed.ncbi.nlm.nih.gov/" + df_pfos["PMID"].astype(str)

df_pfos.to_csv("Rooney_2015_raw.csv", index=False)

df_new = df_pfos[["pmid", "doi", "label_included"]].copy()
df_new["openalex_id"] = None
df_new[["pmid", "doi", "openalex_id", "label_included"]].to_csv(
    "Rooney_2015_ids.csv", index=False
)

df_trans = pd.read_excel(url, sheet_name="Transgenerational")
df_trans["label_included"] = df_trans["Status"].replace({"Excluded": 0, "Included": 1})
df_trans["doi"] = None
df_trans["pmid"] = "https://pubmed.ncbi.nlm.nih.gov/" + df_trans["PMID"].astype(str)

df_trans.to_csv("Walker_2018_raw.csv", index=False)

df_new = df_trans[["pmid", "doi", "label_included"]].copy()
df_new["openalex_id"] = None
df_new[["pmid", "doi", "openalex_id", "label_included"]].to_csv(
    "Walker_2018_ids.csv", index=False
)
