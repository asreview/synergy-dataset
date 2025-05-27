import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
search_in = pd.read_excel(
    "https://zenodo.org/records/7007870/files/Whole%20systematic%20review%20for%20lung%20ca%20v7%20080221.xlsx?download=1",
    engine="openpyxl",
    sheet_name="all ref from endnote",
    header=None,
)

search_1 = search_in.iloc[:6424, :].copy()
search_1.columns = [
    "authors",
    "year",
    "title",
    "journal",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
]

search_2 = search_in.iloc[6424:6450, :].copy()
search_2.columns = [
    "type",
    "empty",
    "empty2",
    "title",
    "A",
    "B",
    "C",
    "D",
    "Link",
    "E",
    "F",
    "G",
]

search_3 = search_in.iloc[6450:6556, :].copy()
search_3.columns = [
    "type",
    "authors",
    "year",
    "title",
    "journal",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "DOI",
]
search_3 = utils.extract_doi(search_3, "DOI")

search = pd.concat([search_1, search_2, search_3])

# FT taken from paper references
inclusions = [
    {"openalex_id": "", "doi": "https://doi.org/10.21037/tcr.2019.11.50"},
    {"openalex_id": "", "doi": "https://doi.org/10.1111/crj.12769"},
    {"openalex_id": "", "doi": "https://doi.org/10.1111/cas.14845"},
    {"openalex_id": "", "doi": "https://doi.org/10.1038/sj.bjc.6605865"},
    {"openalex_id": "", "doi": "https://doi.org/10.1016/j.asjsur.2020.07.025"},
    {"openalex_id": "", "doi": "https://doi.org/10.1002/jcla.24462"},
    {"openalex_id": "", "doi": "https://doi.org/10.1002/prca.202200093"},
    {"openalex_id": "", "doi": "https://doi.org/10.3390/cancers13215482"},
    {"openalex_id": "", "doi": "https://doi.org/10.1073/pnas.1210107109"},
    {"openalex_id": "", "doi": "https://doi.org/10.3233/cbm-130306"},
    {"openalex_id": "", "doi": "https://doi.org/10.1016/s1556-0864(15)30352-x"},
    {"openalex_id": "", "doi": "https://doi.org/10.18632/oncotarget.17477"},
    {"openalex_id": "", "doi": "https://doi.org/10.1155/2013/195692"},
    {"openalex_id": "", "doi": "https://doi.org/10.1016/j.trsl.2021.02.009"},
    {"openalex_id": "", "doi": "https://doi.org/10.1158/1078-0432.ccr-09-3192"},
    {"openalex_id": "", "doi": "https://doi.org/10.3389/fimmu.2021.658922"},
    {"openalex_id": "", "doi": "https://doi.org/10.1074/mcp.ra119.001905"},
    {"openalex_id": "", "doi": "https://doi.org/10.1016/j.cllc.2016.09.012"},
    {"openalex_id": "", "doi": "https://doi.org/10.1007/s00432-020-03325-4"},
    {"openalex_id": "", "doi": "https://doi.org/10.1039/c9cc03620b"},
    {"openalex_id": "", "doi": "https://doi.org/10.1080/2162402x.2019.1625689"},
    {"openalex_id": "", "doi": "https://doi.org/10.1186/s12967-015-0419-y"},
    {"openalex_id": "", "doi": "https://doi.org/10.1371/journal.pone.0032307"},
    {"openalex_id": "", "doi": "https://doi.org/10.3390/cancers12082071"},
    {"openalex_id": "", "doi": "https://doi.org/10.7150/ijbs.36284"},
    {"openalex_id": "", "doi": "https://doi.org/10.1002/jcp.28678"},
    {"openalex_id": "", "doi": "https://doi.org/10.1002/ijc.30727"},
    {"openalex_id": "", "doi": "https://doi.org/10.17219/acem/84935"},
    {"openalex_id": "", "doi": "https://doi.org/10.1177/15330338211041465"},
    {"openalex_id": "", "doi": "https://doi.org/10.1016/j.tranon.2020.100991"},
    {"openalex_id": "", "doi": "https://doi.org/10.1080/01902140902759274"},
    {"openalex_id": "", "doi": "https://doi.org/10.1016/j.lungcan.2009.04.004"},
    {"openalex_id": "", "doi": "https://doi.org/10.1038/modpathol.2010.111"},
    {"openalex_id": "", "doi": "https://doi.org/10.1186/s12943-016-0520-8"},
    {"openalex_id": "", "doi": "https://doi.org/10.1186/s13148-016-0275-5"},
    {"openalex_id": "", "doi": "https://doi.org/10.21873/cgp.20128"},
    {"openalex_id": "", "doi": "https://doi.org/10.1097/jto.0b013e31824ab6b0"},
    {"openalex_id": "", "doi": "https://doi.org/10.1200/jco.21.01460"},
    {"openalex_id": "", "doi": "https://doi.org/10.1186/1471-2407-11-513"},
    {"openalex_id": "", "doi": "https://doi.org/10.1177/10732748221104661"},
    {"openalex_id": "", "doi": "https://doi.org/10.1186/s12885-023-10523-z"},
    {"openalex_id": "", "doi": "https://doi.org/10.1155/2022/1394042"},
    {"openalex_id": "", "doi": "https://doi.org/10.1186/s12951-023-01833-2"},
    {"openalex_id": "", "doi": "https://doi.org/10.3233/cbm-2012-0229"},
    {"openalex_id": "", "doi": "https://doi.org/10.1038/s41598-022-21891-0"},
    {"openalex_id": "", "doi": "https://doi.org/10.1158/1055-9965.epi-10-0467"},
    {"openalex_id": "", "doi": "https://doi.org/10.1111/cas.14387"},
    {"openalex_id": "", "doi": "https://doi.org/10.3390/bios12020127"},
    {"openalex_id": "", "doi": "http://ci.nii.ac.jp/naid/30034122752"},
    {"openalex_id": "", "doi": "https://doi.org/10.1002/prca.201900095"},
    {"openalex_id": "", "doi": "https://doi.org/10.1097/md.0000000000032733"},
    {"openalex_id": "", "doi": "https://doi.org/10.1186/s12890-022-02267-6"},
    {"openalex_id": "", "doi": "https://doi.org/10.18502/ijaai.v21i6.11520"},
    {"openalex_id": "", "doi": "https://doi.org/10.1016/j.clim.2022.109175"},
    {"openalex_id": "", "doi": "https://doi.org/10.1007/s00432-020-03309-4"},
    {"openalex_id": "", "doi": "https://doi.org/10.1164/rccm.201804-0628oc"},
    {"openalex_id": "", "doi": "https://doi.org/10.1002/2211-5463.12878"},
    {"openalex_id": "", "doi": "https://doi.org/10.1186/1476-4598-13-78"},
    {"openalex_id": "", "doi": "https://doi.org/10.1002/jcla.24504"},
    {"openalex_id": "", "doi": "https://doi.org/10.3233/cbm-210099"},
    {"openalex_id": "", "doi": "https://doi.org/10.1080/2162402x.2017.1384108"},
    {"openalex_id": "", "doi": "https://doi.org/10.3389/fimmu.2021.728853"},
    {"openalex_id": "", "doi": "https://doi.org/10.1097/jto.0b013e318299ac32"},
    {"openalex_id": "", "doi": "https://doi.org/10.3390/ijms24054881"},
    {"openalex_id": "", "doi": "https://doi.org/10.1111/1759-7714.13800"},
    {"openalex_id": "", "doi": "https://doi.org/10.1111/1759-7714.13823"},
    {"openalex_id": "", "doi": "https://doi.org/10.1186/s12864-018-4862-z"},
    {"openalex_id": "", "doi": "https://doi.org/10.3389/fgene.2021.673926"},
    {"openalex_id": "", "doi": "https://doi.org/10.1007/s40291-018-0341-0"},
    {"openalex_id": "", "doi": "https://doi.org/10.3233/cbm-190161"},
    {"openalex_id": "", "doi": "https://doi.org/10.1038/s41598-022-22194-0"},
    {"openalex_id": "", "doi": "https://doi.org/10.1007/s00432-013-1555-5"},
    {"openalex_id": "", "doi": "https://doi.org/10.1002/ijc.30822"},
    {"openalex_id": "", "doi": "https://doi.org/10.1016/j.tranon.2016.11.001"},
    {"openalex_id": "", "doi": "https://doi.org/10.3747/co.23.2830"},
    {"openalex_id": "", "doi": "https://doi.org/10.25011/cim.v35i5.18700"},
    {"openalex_id": "", "doi": "https://doi.org/10.32725/jab.2022.004"},
    {"openalex_id": "", "doi": "https://doi.org/10.1002/jcla.24740"},
    {"openalex_id": "", "doi": "https://doi.org/10.3389/fonc.2020.00855"},
    {"openalex_id": "", "doi": "https://doi.org/10.1155/2022/8024700"},
    {"openalex_id": "", "doi": "https://doi.org/10.2147/cmar.s232383"},
    {"openalex_id": "", "doi": "https://doi.org/10.1158/1078-0432.ccr-14-1873"},
    {"openalex_id": "", "doi": "https://doi.org/10.1002/ijc.25289"},
    {"openalex_id": "", "doi": "https://doi.org/10.1155/2022/5501171"},
    {"openalex_id": "", "doi": "https://doi.org/10.1186/s12885-023-10793-7"},
    {"openalex_id": "", "doi": "https://doi.org/10.1186/s13148-020-00828-2"},
    {"openalex_id": "", "doi": "https://doi.org/10.1038/s41598-018-19391-1"},
    {"openalex_id": "", "doi": "https://doi.org/10.1002/cncr.32699"},
    {"openalex_id": "", "doi": "https://doi.org/10.1158/1078-0432.ccr-16-1371"},
    {"openalex_id": "", "doi": "https://doi.org/10.1038/bjc.2014.636"},
    {"openalex_id": "", "doi": "https://doi.org/10.1016/j.lungcan.2008.07.012"},
    {"openalex_id": "", "doi": "https://doi.org/10.3389/fonc.2021.630672"},
    {"openalex_id": "", "doi": "https://doi.org/10.4103/jcrt.jcrt_905_17"},
    {"openalex_id": "https://openalex.org/W2418559992", "doi": ""},
    {"openalex_id": "https://openalex.org/W2194166243", "doi": ""},
]

ft = pd.DataFrame(inclusions)

df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Mohamed_2023", df)
