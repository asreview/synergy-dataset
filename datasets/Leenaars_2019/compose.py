import pandas as pd
from asreview.data import RISReader
import sys

sys.path.append("../../scripts")
import utils

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
    {"pmid": None, "doi": "10.1523/JNEUROSCI.5933-11.2012"},
]

ft = pd.DataFrame(inclusions)

# load RIS files into ASReviewData object
asr_pubmed = RISReader.read_data("https://osf.io/download/m523q/")
asr_embase = RISReader.read_data("https://osf.io/download/exm3a/")

asr_embase = utils.extract_doi(asr_embase, "urls", "doi\/", "&")
asr_embase = utils.extract_pmid(asr_embase, "urls", "pmid\/")

search = pd.concat([asr_embase, asr_pubmed])

df = utils.combine_datafiles(search, ft)

df = utils.extract_doi(df, "doi", "", "&", True)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Leenaars_2019", df)
