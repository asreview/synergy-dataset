import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# get data
# data doi: 10.25340/R4/VB85L1 (download requires extra popup, so using downloaded file)
search = pd.read_excel("data/Ali et al datasets.xlsx", sheet_name="Oliveira")
search = utils.rename_columns(search, title="Title", ti_ab_label="Label")

# FT taken from paper references
inclusions = [
    {"openalex_id": "https://openalex.org/W72245227", "doi": ""},
    {"openalex_id": "", "doi": "https://doi.org/10.1080/1754730X.2014.920135"},
    {"openalex_id": "", "doi": "https://doi.org/10.1007/s12671-016-0603-z"},
    {"openalex_id": "", "doi": "https://doi.org/10.1037/a0027537"},
    {"openalex_id": "", "doi": "https://doi.org/10.1080/10409289.2013.755457"},
    {"openalex_id": "", "doi": " https://doi.org/10.1037/a0018160"},
    {"openalex_id": "", "doi": "https://doi.org/10.11114/jets.v1i2.203"},
    {"openalex_id": "", "doi": "https://doi.org/10.14204/ejrep.43.17068"},
    {"openalex_id": "", "doi": "https://doi.org/10.17105/SPR-2018-0003.V48-1"},
    {"openalex_id": "", "doi": "https://doi.org/10.1177/1063426614532949"},
    {"openalex_id": "", "doi": "https://doi.org/10.1002/pits.21980"},
    {"openalex_id": "", "doi": "https://doi.org/10.1037/ocp0000043"},
    {"openalex_id": "", "doi": "https://doi.org/10.1007/s11121-015-0618-z"},
    {"openalex_id": "", "doi": "https://doi.org/10.3102/0002831208328089"},
    {"openalex_id": "", "doi": "https://doi.org/10.1387/RevPsicodidact.6995"},
    {"openalex_id": "", "doi": "https://doi.org/10.1111/mbe.12026"},
    {"openalex_id": "", "doi": "https://doi.org/10.1007/s12671-013-0246-2"},
    {"openalex_id": "", "doi": "https://doi.org/10.3389/fpsyg.2016.00590"},
    {"openalex_id": "", "doi": "https://doi.org/10.1007/s10464-013-9570-x"},
    {"openalex_id": "", "doi": "https://doi.org/10.1007/s12671-015-0451-2"},
    {"openalex_id": "", "doi": "https://doi.org/10.1177/1476718X15579747"},
    {"openalex_id": "", "doi": "https://doi.org/10.1016/j.jsp.2013.08.001"},
    {"openalex_id": "", "doi": "https://doi.org/10.1037/edu0000187"},
    {"openalex_id": "", "doi": "https://doi.org/10.1037/spq0000035"},
    {"openalex_id": "", "doi": "https://doi.org/10.5539/elt.v7n8p106"},
    {"openalex_id": "", "doi": "https://doi.org/10.1037/a0026118"},
    {"openalex_id": "", "doi": "https://doi.org/10.1080/10409289.2013.825187"},
    {"openalex_id": "", "doi": "https://doi.org/10.1016/j.jsp.2017.10.004"},
    {"openalex_id": "", "doi": "https://doi.org/10.25115/ejrep.v10i28.1530"},
    {"openalex_id": "", "doi": "https://doi.org/10.5944/educxx1.16.1.725"},
    {"openalex_id": "", "doi": "https://doi.org/10.1016/j.ecresq.2007.09.001"},
    {"openalex_id": "", "doi": "https://doi.org/10.1080/01933922.2017.1338811"},
    {"openalex_id": "", "doi": "https://doi.org/10.1007/s11121-012-0305-2"},
    {"openalex_id": "", "doi": "https://doi.org/10.1080/10901027.2019.1638851"},
    {"openalex_id": "", "doi": "https://doi.org/10.1037/a0032093"},
    {"openalex_id": "", "doi": "https://doi.org/10.12973/eu-jer.6.4.565"},
    {"openalex_id": "", "doi": "https://doi.org/10.1016/j.sbspro.2015.01.197"},
    {"openalex_id": "", "doi": "https://doi.org/10.14204/ejrep.31.13073"},
    {"openalex_id": "", "doi": "https://doi.org/10.1007/s12671-020-01304-x"},
    {"openalex_id": "", "doi": "https://doi.org/10.1007/s12671-015-0425-4"},
    {"openalex_id": "", "doi": "https://doi.org/10.1002/smi.2522"},
    {"openalex_id": "", "doi": "https://doi.org/10.1111/j.1469-7610.2007.01861.x"},
    {"openalex_id": "", "doi": "https://doi.org/10.1177/0014402918771321"},
]

ft = pd.DataFrame(inclusions)
ft["label_abstract_included"] = 1

# set labels and turn into single dataframe
df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Oliveira_2021", df)
