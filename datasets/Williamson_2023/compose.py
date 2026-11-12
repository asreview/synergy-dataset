import pandas as pd
from asreview.data import RISReader
import sys

sys.path.append("../../scripts")
import utils

utils.unzip(
    "https://zenodo.org/records/7250310/files/The%20drivers%20of%20lentic%20anguillid%20eel%20movement%20-%20RIS%20files.zip?download=1"
)

search = RISReader.read_data("RIS files - search engine results/Zotero_LER_Export.ris")
search = utils.extract_doi(search, "doi", "", "", True)

inclusions = [
    {"doi": "https://doi.org/10.1111/j.1600-0633.2008.00295.x"},
    {"doi": "https://doi.org/10.1007/s12562-021-01560-3"},
    {"doi": "https://doi.org/10.1111/eff.12371"},
    {"doi": "https://doi.org/10.3390/w13060839"},
    {"doi": "https://doi.org/10.1080/00288330.1983.9515981"},
    {"doi": "https://doi.org/10.1080/00288330.2018.1483955"},
    {"doi": "https://doi.org/10.1023/A:1007639615834"},
    {"doi": "https://doi.org/10.1007/s10641-016-0522-9"},
    {"doi": "https://doi.org/10.1080/00288330.1981.9515915"},
    {"doi": "https://doi.org/10.1007/s00027-019-0671-y"},
    {"doi": "https://doi.org/10.1080/00288330.1999.9516873"},
    {"doi": "https://doi.org/10.1111/j.1095-8649.2008.02167.x"},
    {"doi": "https://doi.org/10.1111/jfb.13335"},
]

ft = pd.DataFrame(inclusions)

df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Williamson_2023", df)
