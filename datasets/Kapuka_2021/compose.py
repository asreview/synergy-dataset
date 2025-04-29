import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# get data
search = pd.read_excel(
    "https://zenodo.org/records/5558905/files/Dataset_primary_search.xlsx?download=1"
)
tiab = pd.read_excel(
    "https://zenodo.org/records/5558905/files/Dataset_secondary_search.xlsx?download=1"
)

search = utils.rename_columns(search, title="Tittle", year="Year of publication")
search = utils.extract_doi(search, "DOI")
tiab = utils.rename_columns(tiab, title="Tittle", year="Year of publication")
tiab = utils.extract_doi(tiab, "DOI")

# FT taken from data (colorcoded)
inclusions = [
    {"doi": "https://doi.org/10.2989/1814232X.2011.637354"},
    {"doi": "https://doi.org/10.1111/acv.12124"},
    {"doi": "https://doi.org/10.1007/s10531-018-1643-6"},
    {"doi": "https://doi.org/10.1007/s10531-010-9836-7"},
    {"doi": "https://doi.org/10.1016/j.cliser.2019.100134"},
    {"doi": "https://doi.org/10.1016/j.cub.2016.12.054"},
    {"doi": "https://doi.org/10.1111/j.1472-4642.2012.00890.x"},
    {"doi": "https://doi.org/10.1016/j.ecolmodel.2015.07.005"},
    {"doi": "https://doi.org/10.1016/j.ecolmodel.2005.11.025"},
    {"doi": "https://doi.org/10.1002/ece3.676"},
    {"doi": "https://doi.org/10.1016/j.flora.2005.06.011"},
    {"doi": "https://doi.org/10.1016/j.foreco.2013.12.032"},
    {"doi": "https://doi.org/10.1186/s40663-016-0080-9"},
    {"doi": "https://doi.org/10.1111/gcb.13739"},
    {"doi": "https://doi.org/10.1111/j.1365-2486.2011.02395.x"},
    {"doi": "https://doi.org/10.4404/hystrix-27.1-11678"},
    {"doi": "https://doi.org/10.1111/j.1365-2664.2012.02157.x"},
    {"doi": "https://doi.org/10.1007/s40333-018-0067-1"},
    {"doi": "https://doi.org/10.1002/2013JG002505"},
    {"doi": "https://doi.org/10.1007/s10336-011-0760-8"},
    {"doi": "https://doi.org/10.3390/land6040073"},
    {"doi": "https://doi.org/10.3354/meps337001"},
    {"doi": "https://doi.org/10.1007/s11258-007-9385-7"},
    {"doi": "https://doi.org/10.1016/j.scitotenv.2018.06.256"},
    {"doi": "https://doi.org/10.1017/S0266467416000584"},
    {"doi": "https://doi.org/10.1111/j.1442-9993.2007.01761.x"},
    {"doi": "https://doi.org/10.1007/s10113-020-01700-y"},
    {"doi": "https://doi.org/10.1080/15481603.2020.1744250"},
]

ft = pd.DataFrame(inclusions)
ft["label_abstract_included"] = 1

# set labels and turn into single dataframe
df = utils.combine_datafiles(search, ft, tiab)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Kapuka_2021", df)
