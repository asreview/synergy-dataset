import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# get search
search = pd.read_csv("https://osf.io/krz3u/download")
search.rename(columns={"label_included": "label_abstract_included"}, inplace=True)
search = utils.extract_doi(search, "DOI")
search = utils.extract_doi(search, "url")

# FT taken from paper references
inclusions = [
    {"openalex_id": "https://openalex.org/W126248063", "doi": ""},
    {"openalex_id": "https://openalex.org/W3090112044", "doi": ""},
    {"openalex_id": "https://openalex.org/W2565099476", "doi": ""},
    {"openalex_id": "https://openalex.org/W2222079638", "doi": ""},
    {"openalex_id": "https://openalex.org/W2182396192", "doi": ""},
    {"openalex_id": "https://openalex.org/W321275225", "doi": ""},
    {"openalex_id": "https://openalex.org/W2128531858", "doi": ""},
    {"openalex_id": "https://openalex.org/W1641141563", "doi": ""},
    {"openalex_id": "https://openalex.org/W2797432737", "doi": ""},
    {"openalex_id": "https://openalex.org/W1888574849", "doi": ""},
    {"openalex_id": "https://openalex.org/W2898593075", "doi": ""},
    {"openalex_id": "https://openalex.org/W2121332991", "doi": ""},
    {"openalex_id": "", "doi": "10.1007/bf02207908"},
    {"openalex_id": "", "doi": "10.1007/BF03025354"},
    {"openalex_id": "", "doi": "10.1007/BF03025662"},
    {"openalex_id": "", "doi": "10.1007/BF03216820"},
    {"openalex_id": "", "doi": "10.1007/s10734-009-9284-z"},
    {"openalex_id": "", "doi": "10.1007/s10734-018-0302-x"},
    {"openalex_id": "", "doi": "10.1016/j.ijintrel.2018.06.003"},
    {"openalex_id": "", "doi": "10.1016/j.teln.2015.12.008"},
    {"openalex_id": "", "doi": "10.1080/03075079.2011.615916"},
    {"openalex_id": "", "doi": "10.1080/03075079.2017.1293874"},
    {"openalex_id": "", "doi": "10.1080/0309877x.2011.569016"},
    {"openalex_id": "", "doi": "10.1080/09518398.2012.736643"},
    {"openalex_id": "", "doi": "10.1080/13562510802452384"},
    {"openalex_id": "", "doi": "10.1080/1360080990210210"},
    {"openalex_id": "", "doi": "10.1080/14675980903371332"},
    {"openalex_id": "", "doi": "10.1080/14708470802303025"},
    {"openalex_id": "", "doi": "10.1080/21568235.2012.743746"},
    {"openalex_id": "", "doi": "10.1080/21568235.2016.1201775"},
    {"openalex_id": "", "doi": "10.1111/j.1465-3435.2008.01369.x"},
    {"openalex_id": "", "doi": "10.11114/jets.v2i3.353"},
    {"openalex_id": "", "doi": "10.1155/2015/202753"},
    {"openalex_id": "", "doi": "10.1177/102831502237638"},
    {"openalex_id": "", "doi": "10.1177/1028315307299422"},
    {"openalex_id": "", "doi": "10.1177/1028315308317937"},
    {"openalex_id": "", "doi": "10.1177/1028315309331390"},
    {"openalex_id": "", "doi": "10.1177/1028315318773137"},
    {"openalex_id": "", "doi": "10.1177/1475240907074788"},
    {"openalex_id": "", "doi": "10.1177/1745499918791362"},
    {"openalex_id": "", "doi": "10.1186/s12909-015-0394-2"},
    {"openalex_id": "", "doi": "10.1186/s12909-016-0549-9"},
    {"openalex_id": "", "doi": "10.1300/J050v15n02_05"},
    {"openalex_id": "", "doi": "10.1353/csd.2013.0010"},
    {"openalex_id": "", "doi": "10.1353/csd.2016.0071"},
    {"openalex_id": "", "doi": "10.3138/jvme.1111-114R"},
    {"openalex_id": "", "doi": "10.32674/jis.v4i1.494"},
    {"openalex_id": "", "doi": "10.32674/jis.v5i4.408"},
    {"openalex_id": "", "doi": "10.32674/jis.v6i1.486"},
    {"openalex_id": "", "doi": "10.32674/jis.v6i4.326"},
    {"openalex_id": "", "doi": "10.32674/jis.v7i2.386"},
    {"openalex_id": "", "doi": "10.32674/jis.v8i2.102"},
    {"openalex_id": "", "doi": "10.32674/jis.v9i1.274"},
    {"openalex_id": "", "doi": "10.3390/educsci7010035"},
    {"openalex_id": "", "doi": "10.3794/johlste.62.160"},
    {"openalex_id": "", "doi": "10.4103/1357-6283.99205"},
    {"openalex_id": "", "doi": "10.5539/hes.v2n3p102"},
    {"openalex_id": "", "doi": "10.5539/ies.v7n8p94"},
    {"openalex_id": "", "doi": "10.5539/ies.v9n4p132"},
    {"openalex_id": "", "doi": "10.5539/jel.v7n2p89"},
    {"openalex_id": "", "doi": "10.5848/apbj.2012.00021"},
    {"openalex_id": "", "doi": "10.7916/d82v2ghj"},
]

ft = pd.DataFrame(inclusions)
ft["label_abstract_included"] = 1
ft = utils.extract_doi(ft, "doi", "", "", True)

# set labels and turn into single dataframe
df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Xu_2022", df)
