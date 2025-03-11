import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# get search
search = pd.read_csv("https://osf.io/q6w5d/download")
search.rename(columns={"label_included": "label_abstract_included"}, inplace=True)
search = utils.extract_doi(search, "url", "", "& ;")
search = utils.extract_pmid(search, "url", "pmid:")

# FT taken from paper references
inclusions = [
    {"doi": "https://doi.org/10.1016/j.lindif.2013.01.007"},
    {"doi": "https://doi.org/10.1016/j.learninstruc.2014.12.003"},
    {"doi": "https://doi.org/10.1016/j.learninstruc.2020.101367"},
    {"doi": "https://doi.org/10.1007/s11251-015-9359-4"},
    {"doi": "https://doi.org/10.1080/07370008.2011.636495"},
    {"doi": "https://doi.org/10.1016/j.lindif.2013.12.012"},
    {"doi": "https://doi.org/10.1111/jcal.12162"},
    {"doi": "https://doi.org/10.1111/1467-9817.12247"},
    {"doi": "https://doi.org/10.1111/bjep.12005"},
    {"doi": "https://doi.org/10.1016/j.cedpsych.2016.07.004"},
    {"doi": "https://doi.org/10.1598/RRQ.44.1.1"},
    {"doi": "https://doi.org/10.1016/j.learninstruc.2010.02.002"},
    {"doi": "https://doi.org/10.1207/S1532690XC12004_2"},
    {"doi": "https://doi.org/10.1002/tea.21172"},
    {"doi": "https://doi.org/10.1007/s11145-020-10030-8"},
    {"doi": "https://doi.org/10.1016/S0747-5632(03)00021-9"},
    {"doi": "https://doi.org/10.1111/bjep.12288"},
    {"doi": "https://doi.org/10.1080/10508406.2011.582376"},
    {"doi": "https://doi.org/10.1111/bjep.12278"},
    {"doi": "https://doi.org/10.1080/11356405.2019.1601937"},
    {"doi": "https://doi.org/10.1016/j.chb.2012.10.012"},
    {"doi": "https://doi.org/10.1177/0735633120952731"},
    {"doi": "https://doi.org/10.1080/0163853X.2016.1169968"},
    {"doi": "https://doi.org/10.1016/j.compedu.2016.07.001"},
    {"doi": "https://doi.org/10.1177/107769901108800403"},
    {"doi": "https://doi.org/10.1007/s11251-013-9276-3"},
    {"doi": "https://doi.org/10.13016/M2XW4H"},
    {"doi": "https://doi.org/10.1080/0163853X.2016.1174654"},
    {"doi": "https://doi.org/10.1016/j.cedpsych.2019.03.003"},
    {"doi": "https://doi.org/10.1007/s11145-018-9863-4"},
    {"doi": "https://doi.org/10.1002/asi.22743"},
    {"doi": "https://doi.org/10.1080/07370008.2013.769995"},
    {"doi": "https://doi.org/10.1080/02103702.2019.1690849"},
    {"doi": "https://doi.org/10.1016/j.compedu.2014.03.016"},
    {"doi": "https://doi.org/10.1016/j.lindif.2017.07.002"},
    {"doi": "https://doi.org/10.1016/j.compedu.2017.12.009"},
    {"doi": "https://doi.org/10.1111/jcal.12399"},
    {"doi": "https://doi.org/10.1037/edu0000057"},
    {"doi": "https://doi.org/10.1016/j.cedpsych.2020.101900"},
    {"doi": "https://doi.org/10.1016/j.lindif.2017.01.021"},
    {"doi": "https://doi.org/10.1080/02103702.2018.1480458"},
    {"doi": "https://doi.org/10.1080/0163853X.2017.1402165"},
    {"doi": "https://doi.org/10.1080/00220973.2018.1496058"},
    {"doi": "https://doi.org/10.1080/02103702.2019.1690848"},
    {"doi": "https://doi.org/10.1207/s1532690xci1501_3"},
    {"doi": "https://doi.org/10.1016/j.cedpsych.2017.12.002"},
    {"doi": "https://doi.org/10.1016/j.chb.2013.04.034"},
    {"doi": "https://doi.org/10.1002/asi.23585"},
    {"doi": "https://doi.org/10.1016/j.compedu.2019.103796"},
    {"doi": "https://doi.org/10.1007/s11145-018-9868-z"},
    {"doi": "https://doi.org/10.1080/02702711.2016.1278417"},
    {"doi": "https://doi.org/10.1080/00313831.2018.1434828"},
    {"doi": "https://doi.org/10.1007/s11145-020-10041-5"},
    {"doi": "https://doi.org/10.1016/j.learninstruc.2009.02.001"},
    {"doi": "https://doi.org/10.1080/01443410.2010.538039"},
    {"doi": "https://doi.org/10.1080/11356405.2019.1597442"},
    {"doi": "https://doi.org/10.1177/0735633115599604"},
    {"doi": "https://doi.org/10.1177/0093650214565915"},
    {"doi": "https://doi.org/10.1016/j.chb.2016.02.057"},
    {"doi": "https://doi.org/10.1007/s11145-015-9601-0"},
    {"doi": "https://doi.org/10.1111/jcc4.12006"},
    {"doi": "https://doi.org/10.1016/j.learninstruc.2019.101266"},
    {"doi": "https://doi.org/10.1037/0022-0663.83.1.73"},
    {"doi": "https://doi.org/10.1111/j.1083-6101.2012.01596.x"},
]

ft = pd.DataFrame(inclusions)
ft["label_abstract_included"] = 1

# set labels and turn into single dataframe
df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Anmarkrud_2021", df)
