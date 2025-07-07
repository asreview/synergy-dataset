import pandas as pd
import sys
import re
from urllib.request import urlopen

sys.path.append("../../scripts")
import utils

# Read input
wos1 = pd.read_excel(
    "https://zenodo.org/records/8348665/files/ECM&ICIs&marker_wos.xls?download=1"
)
wos2 = pd.read_excel(
    "https://zenodo.org/records/8348665/files/ECM&ICIs_wos.xls?download=1"
)
wos3 = pd.read_excel(
    "https://zenodo.org/records/8348665/files/matrixRemodeling&ICIS_wos.xls?download=1"
)
wos4 = pd.read_excel(
    "https://zenodo.org/records/8348665/files/matrixRemodeling&immunoth_wos.xls?download=1"
)
wos = pd.concat([wos1, wos2, wos3, wos4])
wos = utils.extract_doi(wos, "DOI")
wos = utils.extract_pmid(wos, "Pubmed Id")
wos = utils.rename_columns(wos, title="Article Title", year="Publication Year")

sco1 = pd.read_csv(
    "https://zenodo.org/records/8348665/files/ECM&ICIs_scopus.csv?download=1"
)
sco3 = pd.read_csv(
    "https://zenodo.org/records/8348665/files/ECM&immunother_scopus.csv?download=1"
)
sco4 = pd.read_csv(
    "https://zenodo.org/records/8348665/files/matrixRemodeling&ICIs_scopus.csv?download=1"
)
sco5 = pd.read_csv(
    "https://zenodo.org/records/8348665/files/matrixRemodeling&immunother_scopus.csv?download=1"
)

sco = pd.concat([sco1, sco3, sco4, sco5])
sco = utils.extract_doi(sco, "DOI")
sco = utils.rename_columns(sco, title="Title", year="Year")

sco2 = pd.read_csv(
    "https://zenodo.org/records/8348665/files/ECM&immunoth&marker_scopus.csv?download=1",
    sep="\t",
    encoding = "ISO-8859-1"
)
sco2 = utils.extract_doi(sco2, "DOI", "", "&")
sco2 = utils.extract_doi(sco2, "DOI.1", "", "&")
sco2 = utils.extract_pmid(sco2, "PMID")
for i in range(25):
    if i not in [8, 11, 12]:
        column_name = "Unnamed: " + str(i + 15)
        sco2 = utils.extract_doi(sco2, column_name, "", "&")

pubs = [
    "https://zenodo.org/records/8348665/files/summary-ECM&ICI_pubmed.txt?download=1",
    "https://zenodo.org/records/8348665/files/summary-ECM&immunother_pubmed.txt?download=1",
    "https://zenodo.org/records/8348665/files/summary-ECMremodeling&ICI_pubmed.txt?download=1",
    "https://zenodo.org/records/8348665/files/summary-ICI&ECM&marker_pubmed.txt?download=1",
    "https://zenodo.org/records/8348665/files/summary-matrix_remodeling&immunother_pubmed.txt?download=1",
]

pmids = []

# files are in pubmed txt file, we aim to just extract the pmid
for filename in pubs:
    file = urlopen(filename)
    current_entry_text = ""
    next_entry_nr = 1
    # loop over lines and concatenate separate entries to 1 line so we can extract from it
    for line in file:
        line = line.decode("utf-8").strip()
        if line.startswith(str(next_entry_nr) + ": "):
            if next_entry_nr > 1:
                # Do the extraction for previous line
                if "PMID" in current_entry_text:
                    pm = re.search(r"PMID:\s*(\d+)", current_entry_text)
                    if pm:
                        pmids.append(pm.group(1))
            current_entry_text = line
            next_entry_nr += 1
        else:
            current_entry_text += line

    # process final line
    if "PMID" in current_entry_text:
        pm = re.search(r"PMID:\s*(\d+)", current_entry_text)
        if pm:
            pmids.append(pm.group(1))
    file.close()

data = {"PMID": pmids}

pub = pd.DataFrame(data)
pub = utils.extract_pmid(pub, "PMID")

search = pd.concat([wos, sco, sco2, pub])

# FT taken from paper references
inclusions = [
    {"doi": "https://doi.org/10.3389/fgene.2022.1085785"},
    {"doi": "https://doi.org/10.3389/fonc.2021.729230"},
    {"doi": "https://doi.org/10.7717/peerj.9736"},
    {"doi": "https://doi.org/10.1080/2162402X.2021.2020984"},
    {"doi": "https://doi.org/10.3389/fgene.2022.765569"},
    {"doi": "https://doi.org/10.1155/2022/7904982"},
    {"doi": "https://doi.org/10.1155/2022/6419695"},
    {"doi": "https://doi.org/10.5152/tud.2020.20062"},
    {"doi": "https://doi.org/10.1155/2020/8825997"},
    {"doi": "https://doi.org/10.1038/s41586-021-04057-2"},
    {"doi": "https://doi.org/10.3389/fimmu.2022.859581"},
    {"doi": "https://doi.org/10.3389/fimmu.2021.714230"},
    {"doi": "https://doi.org/10.3389/fmed.2022.981074"},
    {"doi": "https://doi.org/10.3389/pore.2022.1610350"},
    {"doi": "https://doi.org/10.3389/fgene.2022.900124"},
    {"doi": "https://doi.org/10.1186/s13046-022-02271-y"},
    {"doi": "https://doi.org/10.1016/j.brainresbull.2021.07.013"},
    {"doi": "https://doi.org/10.3389/fgene.2022.1058207"},
    {"doi": "https://doi.org/10.1007/s00428-021-03193-4"},
    {"doi": "https://doi.org/10.1002/hep.31600"},
    {"doi": "https://doi.org/10.1038/s41598-022-17954-x"},
    {"doi": "https://doi.org/10.1155/2022/2592962"},
    {"doi": "https://doi.org/10.1002/1878-0261.12912"},
    {"doi": "https://doi.org/10.1097/MD.0000000000032444"},
    {"doi": "https://doi.org/10.3389/fgene.2022.864655"},
    {"doi": "https://doi.org/10.3389/fonc.2021.592854"},
    {"doi": "https://doi.org/10.1038/s41467-020-17395-y"},
    {"doi": "https://doi.org/10.15252/emmm.202013270"},
    {"doi": "https://doi.org/10.1158/2326-6066.CIR-20-0074"},
    {"doi": "https://doi.org/10.3389/fimmu.2022.824586"},
    {"doi": "https://doi.org/10.1016/j.celrep.2022.111201"},
    {"doi": "https://doi.org/10.7150/thno.61209"},
    {"doi": "https://doi.org/10.1038/modpathol.2010.154"},
    {"doi": "https://doi.org/10.1182/blood-2016-03-705780"},
    {"doi": "https://doi.org/10.4049/jimmunol.1700529"},
    {"doi": "https://doi.org/10.3389/fonc.2021.761030"},
    {"doi": "https://doi.org/ 10.1080/15384101.2022.2154551"},
    {"doi": "https://doi.org/10.3390/cancers12102786"},
    {"doi": "https://doi.org/10.1186/s40425-018-0474-z"},
    {"doi": "https://doi.org/10.1136/jitc-2020-001193"},
    {"doi": "https://doi.org/10.1038/s41467-020-18298-8"},
    {"doi": "https://doi.org/10.3389/fcell.2021.721897"},
    {"doi": "https://doi.org/10.3390/ijms22147511"},
    {"doi": "https://doi.org/10.1038/s42003-021-01911-x"},
    {"doi": "https://doi.org/10.3892/ol.2021.13091"},
    {"doi": "https://doi.org/10.1371/journal.pone.0245287"},
    {"doi": "https://doi.org/10.1002/2211-5463.13541"},
]

ft = pd.DataFrame(inclusions)

df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Fejza_2023", df)
