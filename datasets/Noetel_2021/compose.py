import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# get search
search = pd.read_csv("https://osf.io/3w4qa/download")
search.rename(columns={"label_included": "label_abstract_included"}, inplace=True)

# FT taken from paper references
inclusions = [
    {"doi": "https://doi.org/10.1037/a0026147", "openalex_id": "nan"},
    {"doi": "https://doi.org/10.1016/j.compedu.2018.06.023", "openalex_id": "nan"},
    {"doi": "https://doi.org/10.1007/s11423-020-09748-7", "openalex_id": "nan"},
    {"doi": "nan", "openalex_id": "https://openalex.org/W2590206292"},
    {"doi": "https://doi.org/10.1016/j.compedu.2016.06.005", "openalex_id": "nan"},
    {"doi": "https://doi.org/10.1016/j.edurev.2018.09.004", "openalex_id": "nan"},
    {"doi": "https://doi.org/10.1007/s10648-020-09587-1", "openalex_id": "nan"},
    {"doi": "nan", "openalex_id": "https://openalex.org/W2903037897"},
    {"doi": "https://doi.org/10.1016/j.edurev.2018.05.002", "openalex_id": "nan"},
    {"doi": "https://doi.org/10.1016/j.learninstruc.2005.07.001", "openalex_id": "nan"},
    {"doi": "https://doi.org/10.1016/j.learninstruc.2006.10.001", "openalex_id": "nan"},
    {"doi": "https://doi.org/10.1007/s10648-013-9228-0", "openalex_id": "nan"},
    {"doi": "https://doi.org/10.1007/s10648-010-9126-7", "openalex_id": "nan"},
    {"doi": "https://doi.org/10.4018/978-1-5225-7663-1.ch028", "openalex_id": "nan"},
    {"doi": "https://doi.org/10.32890/mjli2019.16.1.6", "openalex_id": "nan"},
    {"doi": "https://dl.acm.org/doi/proceedings/10.5555/1562524", "openalex_id": "nan"},
    {"doi": "https://doi.org/10.1016/j.system.2013.07.013", "openalex_id": "nan"},
    {"doi": "https://doi.org/10.5539/ies.v8n13p73", "openalex_id": "nan"},
    {"doi": "https://doi.org/10.1007/s10936-011-9180-4", "openalex_id": "nan"},
    {"doi": "https://doi.org/10.1016/j.edurev.2012.05.003", "openalex_id": "nan"},
    {"doi": "https://doi.org/10.1007/s10648-018-9456-4", "openalex_id": "nan"},
    {"doi": "https://doi.org/10.1016/j.edurev.2015.12.003", "openalex_id": "nan"},
    {"doi": "https://doi.org/10.1016/j.edurev.2017.11.001", "openalex_id": "nan"},
    {"doi": "https://doi.org/10.2190/EC.49.1.a", "openalex_id": "nan"},
    {"doi": "https://doi.org/10.1007/s10648-018-9435-9", "openalex_id": "nan"},
    {"doi": "https://doi.org/10.1037/edu0000372", "openalex_id": "nan"},
    {"doi": "https://doi.org/10.1007/s10648-020-09522-4", "openalex_id": "nan"},
    {"doi": "https://doi.org/10.3724/sp.j.1041.2016.00540", "openalex_id": "nan"},
    {"doi": "https://doi.org/10.1371/journal.pone.0183884", "openalex_id": "nan"},
]

ft = pd.DataFrame(inclusions)
ft["label_abstract_included"] = 1

# set labels and turn into single dataframe
df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Noetel_2021", df)
