import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
search = pd.read_csv(
    "https://zenodo.org/records/6400078/files/ms-slr-unit-ac-testing_11-21-final-pool-classified.csv?download=1"
)

# FT taken from paper references
inclusions = [
    {"openalex_id": "https://openalex.org/W3126344064", "doi": ""},
    {"openalex_id": "", "doi": "https://doi.org/10.1109/ICST.2013.14"},
    {"openalex_id": "", "doi": "https://doi.org/10.1007/s10664-013-9293-5"},
    {"openalex_id": "", "doi": "https://doi.org/10.1186/s13173-015-0034-z"},
    {"openalex_id": "", "doi": "https://doi.org/10.1002/stvr.1479"},
    {"openalex_id": "", "doi": "https://doi.org/10.1145/2554850.2555054"},
    {"openalex_id": "", "doi": "https://doi.org/10.1007/s10664-014-9313-0"},
    {"openalex_id": "", "doi": "https://doi.org/10.1007/978-3-319-18612-2_23"},
    {"openalex_id": "", "doi": "https://doi.org/10.1109/ICST.2012.115"},
    {"openalex_id": "", "doi": "https://doi.org/10.1109/WETSoM.2017.2"},
    {"openalex_id": "", "doi": "https://doi.org/10.1109/VST50071.2020.9051632"},
    {"openalex_id": "", "doi": "https://doi.org/10.1109/MS.2011.117"},
    {"openalex_id": "", "doi": "https://doi.org/10.1109/ISSRE.2014.11"},
    {"openalex_id": "", "doi": "https://doi.org/10.1007/s10664-019-09692-y"},
    {"openalex_id": "", "doi": "https://doi.org/10.1007/s00766-014-0208-9"},
    {"openalex_id": "", "doi": "https://doi.org/10.1145/2483760.2483774"},
    {"openalex_id": "", "doi": "https://doi.org/10.1109/TSE.2016.2616877"},
    {"openalex_id": "", "doi": "https://doi.org/10.1145/3324884.3421843"},
    {"openalex_id": "", "doi": "https://doi.org/10.1016/j.scico.2012.02.006"},
    {"openalex_id": "", "doi": "https://doi.org/10.1145/3379597.3387471"},
    {"openalex_id": "", "doi": "https://doi.org/10.1109/MSR.2017.8"},
    {"openalex_id": "", "doi": "https://doi.org/10.1145/3144763.3144765"},
    {"openalex_id": "", "doi": "https://doi.org/10.1109/AGILE.2011.37"},
    {"openalex_id": "", "doi": "https://doi.org/10.1145/2851613.2851807"},
    {"openalex_id": "", "doi": "https://doi.org/10.1145/2593501.2593507"},
    {"openalex_id": "", "doi": "https://doi.org/10.1007/978-3-642-40888-5_6"},
    {"openalex_id": "", "doi": "https://doi.org/10.4230/LIPIcs.ECOOP.2018.5"},
    {"openalex_id": "", "doi": "https://doi.org/10.1007/s10664-013-9281-9"},
    {"openalex_id": "", "doi": "https://doi.org/10.1109/ICSE.2015.348"},
    {"openalex_id": "", "doi": "https://doi.org/10.18293/SEKE2019-102"},
    {"openalex_id": "", "doi": "https://doi.org/10.1145/3194095.3194102"},
    {"openalex_id": "", "doi": "https://doi.org/10.1109/ICSTW.2014.29"},
    {"openalex_id": "", "doi": "https://doi.org/10.1145/2785592.2795365"},
    {"openalex_id": "", "doi": "https://doi.org/10.1109/MCSE.2018.05329819"},
    {"openalex_id": "", "doi": "https://doi.org/10.1109/APSEC.2014.10"},
    {"openalex_id": "", "doi": "https://doi.org/10.1109/TSE.2020.3027522"},
    {"openalex_id": "", "doi": "https://doi.org/10.1145/3383219.3383236"},
    {"openalex_id": "", "doi": "https://doi.org/10.1016/j.jss.2018.03.052"},
    {"openalex_id": "", "doi": "https://doi.org/10.1016/j.infsof.2017.07.005"},
    {"openalex_id": "", "doi": "https://doi.org/10.1145/3019612.3019830"},
    {"openalex_id": "", "doi": "https://doi.org/10.1109/REW.2017.50"},
    {"openalex_id": "", "doi": "https://doi.org/10.1109/ICST.2019.00040"},
    {"openalex_id": "", "doi": "https://doi.org/10.1145/2896921.2896927"},
    {"openalex_id": "", "doi": "https://doi.org/10.1109/ICSM.2013.12"},
    {"openalex_id": "", "doi": "https://doi.org/10.1145/3202710.3203153"},
    {"openalex_id": "", "doi": "https://doi.org/10.1016/j.jss.2019.110421"},
    {"openalex_id": "", "doi": "https://doi.org/10.1007/978-3-319-67113-0_4"},
    {"openalex_id": "", "doi": "https://doi.org/10.1016/j.infsof.2020.106311"},
]

ft = pd.DataFrame(inclusions)

search = utils.rename_columns(search, title="Title", year="Year")
search = utils.extract_doi(search, "DOI")

df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("van_Heugten_Breurkes_2022", df)
