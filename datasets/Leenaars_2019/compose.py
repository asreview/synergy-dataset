import pandas as pd
from asreview import ASReviewData

import urllib.parse


key = "Leenaars_2019"


def unquote_nan(x):
    try:
        return urllib.parse.unquote(urllib.parse.unquote(x))
    except Exception:
        return None

inclusions = [
    {"pmid": None, "doi": "10.1016/0304-3940(96)12918-9"},
    {"pmid": None, "doi": "10.1016/j.neures.2004.05.001"},
    {"pmid": None, "doi": "10.1016/j.bbr.2007.03.018"},
    {"pmid": "https://pubmed.ncbi.nlm.nih.gov/12162531", "doi": None},
    {"pmid": None, "doi": "10.1152/ajpregu.90541.2008"},
    {"pmid": None, "doi": "10.1097/00001756-199703240-00025"},
    {"pmid": None, "doi": "10.1016/S0006-8993(97)01308-5"},
    {"pmid": None, "doi": "10.1002/jnr.20602"},
    {"pmid": None, "doi": "10.1016/j.arcmed.2006.07.004"},
    {"pmid": None, "doi": "10.1152/ajpregu.1997.273.1.R451"},
    {"pmid": None, "doi": "10.1016/S0306-4522(96)00549-0"},
    {"pmid": None, "doi": "10.1016/S0306-4522(02)00158-6"},
    {"pmid": None, "doi": "10.1523/JNEUROSCI.5674-10.2011"},
    {"pmid": None, "doi": "10.5665/sleep.2106"},
    {"pmid": None, "doi": "10.1111/j.1471-4159.2011.07350.x"},
    {"pmid": None, "doi": "10.1080/01616412.2015.1114231"},
    {"pmid": None, "doi": "10.1523/JNEUROSCI.5933-11.2012"}
]

df_inclusions = pd.DataFrame(inclusions)

# load RIS files into ASReviewData object
asr_pubmed = ASReviewData.from_file("https://osf.io/download/m523q/")
asr_embase = ASReviewData.from_file("https://osf.io/download/exm3a/")

asr_embase.df["doi"] = asr_embase.df["url"].str.extract(r"doi\/(10.\S+?)&")[0].apply(unquote_nan)
asr_embase.df["pmid"] = "https://pubmed.ncbi.nlm.nih.gov/" + asr_embase.df["url"].str.extract(r"pmid\/(\d+)&")[0]

# set labels and turn into single dataframe
df_inclusions["label_included"] = 1
asr_pubmed.df["label_included"] = 0
asr_embase.df["label_included"] = 0
df = pd.concat([df_inclusions, asr_pubmed.df, asr_embase.df], ignore_index=True)

# adjust columns and drop missing and duplicate ids
df["doi"] = "https://doi.org/" + df["doi"].str.extract(r"(10.\S+)")
df["doi"] = df["doi"].str.split("&", n = 1, expand = True)[0]

# save results to file
df.to_csv(f"{key}_raw.csv", index=False)

df_new = df[["pmid", "doi", "label_included"]].copy()
df_new["openalex_id"] = None

df_new[["pmid", "doi", "openalex_id", "label_included"]].to_csv(f"{key}_ids.csv", index=False)
