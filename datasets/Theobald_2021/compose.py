import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# get search
search = pd.read_csv("https://osf.io/3hf5s/download")
search.rename(columns={"label_included": "label_abstract_included"}, inplace=True)
search = utils.extract_doi(search, "DOI")

# FT taken from paper references
inclusions = [
    {"openalex_id": "https://openalex.org/W2168406945", "doi": ""},
    {"openalex_id": "https://openalex.org/W2522978391", "doi": ""},
    {"openalex_id": "https://openalex.org/W2585138354", "doi": ""},
    {"openalex_id": "https://openalex.org/W2729425366", "doi": ""},
    {"openalex_id": "https://openalex.org/W3039329067", "doi": ""},
    {"openalex_id": "https://openalex.org/W598285045", "doi": ""},
    {"openalex_id": "https://openalex.org/W612752139", "doi": ""},
    {"openalex_id": "", "doi": "10.1007/s10212-010-0020-y"},
    {"openalex_id": "", "doi": "10.1007/s10212-013-0196-z"},
    {"openalex_id": "", "doi": "10.1007/s11423-020-09781-6"},
    {"openalex_id": "", "doi": "10.1016/j.cedpsych.205.02.002"},
    {"openalex_id": "", "doi": "10.1016/j.iheduc.2016.07.002"},
    {"openalex_id": "", "doi": "10.1016/j.ijer.2016.05.010"},
    {"openalex_id": "", "doi": "10.1016/j.jarmac.2020.03.004"},
    {"openalex_id": "", "doi": "10.1016/s0005-7894(75)80107-9"},
    {"openalex_id": "", "doi": "10.1024//1010-0652.15.34.181"},
    {"openalex_id": "", "doi": "10.1024/1010-0652/a000022"},
    {"openalex_id": "", "doi": "10.1037/0022-0167.25.5.376"},
    {"openalex_id": "", "doi": "10.1037/0022-0167.33.2.131"},
    {"openalex_id": "", "doi": "10.1037/0022-0663.71.1.64"},
    {"openalex_id": "", "doi": "10.1037/0022-0663.83.1.134"},
    {"openalex_id": "", "doi": "10.1037/edu0000405"},
    {"openalex_id": "", "doi": "10.1037/edu0000485"},
    {"openalex_id": "", "doi": "10.1037/edu0000624"},
    {"openalex_id": "", "doi": "10.1080/00220671.1977.10885028"},
    {"openalex_id": "", "doi": "10.1080/00220973.1983.11011847"},
    {"openalex_id": "", "doi": "10.1080/07294360.2014.935932"},
    {"openalex_id": "", "doi": "10.1080/09515070601106471"},
    {"openalex_id": "", "doi": "10.1080/10790195.2015.1032041"},
    {"openalex_id": "", "doi": "10.1177/1362168809341511"},
    {"openalex_id": "", "doi": "10.1177/1362168812457528"},
    {"openalex_id": "", "doi": "10.1207/s15326985ep2003_5"},
    {"openalex_id": "", "doi": "10.1353/csd.2003.0034"},
    {"openalex_id": "", "doi": "10.1515/cjal-2017-0014"},
    {"openalex_id": "", "doi": "10.24355/dbbs.084-201208311158-0"},
]

ft = pd.DataFrame(inclusions)
ft["label_abstract_included"] = 1
ft = utils.extract_doi(ft, "doi", "", "", True)

# set labels and turn into single dataframe
df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Theobald_2021", df)
