import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

search = pd.read_excel(
    "https://static-content.springer.com/esm/art%3A10.1186%2Fs13643-016-0263-z/MediaObjects/13643_2016_263_MOESM1_ESM.xlsx",
    sheet_name="BPA",
)
search = utils.extract_pmid(search, "PMID")

# FT taken from paper
inclusions = [
    {"openalex_id": "https://openalex.org/W2327758174"},
    {"openalex_id": "https://openalex.org/W1995084475"},
    {"openalex_id": "https://openalex.org/W1964818491"},
    {"openalex_id": "https://openalex.org/W2011868725"},
    {"openalex_id": "https://openalex.org/W2060448730"},
    {"openalex_id": "https://openalex.org/W2105005092"},
    {"openalex_id": "https://openalex.org/W2044598637"},
    {"openalex_id": "https://openalex.org/W1982942271"},
    {"openalex_id": "https://openalex.org/W2153716114"},
    {"openalex_id": "https://openalex.org/W2057168469"},
    {"openalex_id": "https://openalex.org/W1985569861"},
    {"openalex_id": "https://openalex.org/W2013783788"},
    {"openalex_id": "https://openalex.org/W2028466984"},
    {"openalex_id": "https://openalex.org/W2024829332"},
    {"openalex_id": "https://openalex.org/W2138484830"},
    {"openalex_id": "https://openalex.org/W2008171863"},
    {"openalex_id": "https://openalex.org/W2156112336"},
    {"openalex_id": "https://openalex.org/W1992629360"},
    {"openalex_id": "https://openalex.org/W2167384747"},
    {"openalex_id": "https://openalex.org/W2039711181"},
    {"openalex_id": "https://openalex.org/W1966357969"},
    {"openalex_id": "https://openalex.org/W2120526208"},
    {"openalex_id": "https://openalex.org/W2088344644"},
    {"openalex_id": "https://openalex.org/W1989873377"},
    {"openalex_id": "https://openalex.org/W2037278965"},
    {"openalex_id": "https://openalex.org/W2163478251"},
    {"openalex_id": "https://openalex.org/W2024201289"},
    {"openalex_id": "https://openalex.org/W2085280717"},
    {"openalex_id": "https://openalex.org/W2007586461"},
    {"openalex_id": "https://openalex.org/W2092671830"},
    {"openalex_id": "https://openalex.org/W2068630231"},
    {"openalex_id": "https://openalex.org/W2071994059"},
    {"openalex_id": "https://openalex.org/W2047523002"},
    {"openalex_id": "https://openalex.org/W2074587538"},
    {"openalex_id": "https://openalex.org/W2016258313"},
    {"openalex_id": "https://openalex.org/W2116247529"},
    {"openalex_id": "https://openalex.org/W2072384141"},
    {"openalex_id": "https://openalex.org/W1986519131"},
    {"openalex_id": "https://openalex.org/W2014316289"},
    {"openalex_id": "https://openalex.org/W1967446178"},
    {"openalex_id": "https://openalex.org/W2017707375"},
    {"openalex_id": "https://openalex.org/W2163044427"},
    {"openalex_id": "https://openalex.org/W2039021795"},
    {"openalex_id": "https://openalex.org/W1985942833"},
]

ft = pd.DataFrame(inclusions)

# set labels and turn into single dataframe
df = utils.combine_datafiles(search, ft)

df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Wassenaar_2017", df)
