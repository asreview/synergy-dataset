import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# get data
# data doi: 10.25340/R4/VB85L1 (download requires extra popup, so using downloaded file)
search = pd.read_excel("data/Ali et al datasets.xlsx", sheet_name="Ward")
search = utils.rename_columns(search, title="Title", ti_ab_label="Label")

# FT taken from paper references
inclusions = [
    {"openalex_id": "https://openalex.org/W2131509292", "doi": ""},
    {"openalex_id": "https://openalex.org/W1580052515", "doi": ""},
    {"openalex_id": "https://openalex.org/W1536189362", "doi": ""},
    {"openalex_id": "https://openalex.org/W2734982186", "doi": ""},
    {"openalex_id": "https://openalex.org/W2157808176", "doi": ""},
    {"openalex_id": "https://openalex.org/W3101483539", "doi": ""},
    {"openalex_id": "https://openalex.org/W2772332671", "doi": ""},
    {"openalex_id": "https://openalex.org/W2125736864", "doi": ""},
    {"openalex_id": "", "doi": "https://doi.org/10.1002/pits.21803"},
    {"openalex_id": "", "doi": "https://doi.org/10.1007/BF00925822"},
    {"openalex_id": "", "doi": "https://doi.org/10.1007/s12310-017-9217-4"},
    {"openalex_id": "", "doi": "https://doi.org/10.1037/a0024655"},
    {"openalex_id": "", "doi": "https://doi.org/10.1037/a0026001"},
    {"openalex_id": "", "doi": "https://doi.org/10.1080/16823206.2015.1024146"},
    {"openalex_id": "", "doi": "https://doi.org/10.1177/00222194020350060601"},
    {"openalex_id": "", "doi": "https://doi.org/10.1177/019874290703200202"},
    {"openalex_id": "", "doi": "https://doi.org/10.1177/1087054708329972"},
    {"openalex_id": "", "doi": "https://doi.org/10.1177/1087054712453171"},
    {"openalex_id": "", "doi": "https://doi.org/10.1177/1087054715603198"},
    {"openalex_id": "", "doi": "https://doi.org/10.1177/1087054716658124"},
    {"openalex_id": "", "doi": "https://doi.org/10.1177/1087054717707045"},
    {"openalex_id": "", "doi": "https://doi.org/10.1177/108705479800200411"},
    {"openalex_id": "", "doi": "https://doi.org/10.1186/s13034-017-0153-8"},
    {"openalex_id": "", "doi": "https://doi.org/10.13109/prkk.2016.65.5.315"},
    {"openalex_id": "", "doi": "https://doi.org/10.3389/fpsyg.2017.01157"},
    {"openalex_id": "", "doi": "https://doi.org/10.5539/ass.v11n10p212"},
    {"openalex_id": "", "doi": "https://doi.org/10.9790/1959-0506072937"},
]

ft = pd.DataFrame(inclusions)
ft["label_abstract_included"] = 1

# set labels and turn into single dataframe
df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Ward_2020", df)
