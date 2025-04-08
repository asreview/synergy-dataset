import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# get search
search = pd.read_csv("https://osf.io/mjygr/download")
search.rename(columns={"label_included": "label_abstract_included"}, inplace=True)
search = utils.extract_doi(search, "DOI")
search["url"] = search["url"].astype(str)
search["url"] = search["url"].apply(lambda x: "&".join(x.split("http")))
search = utils.extract_doi(search, "url", "", "&")

# FT taken from paper references
inclusions = [
    {"openalex_id": "https://openalex.org/works/w117552264"},
    {"openalex_id": "https://openalex.org/works/w1484411757"},
    {"openalex_id": "https://openalex.org/works/w1528950336"},
    {"openalex_id": "https://openalex.org/works/w1555486138"},
    {"openalex_id": "https://openalex.org/works/w188778733"},
    {"openalex_id": "https://openalex.org/works/w1963740746"},
    {"openalex_id": "https://openalex.org/works/w1986027646"},
    {"openalex_id": "https://openalex.org/works/w2013055978"},
    {"openalex_id": "https://openalex.org/works/w2054421127"},
    {"openalex_id": "https://openalex.org/works/w213026570"},
    {"openalex_id": "https://openalex.org/works/w2139731049"},
    {"openalex_id": "https://openalex.org/works/w2431964556"},
    {"openalex_id": "https://openalex.org/works/w2469908846"},
    {"openalex_id": "https://openalex.org/works/w2525545930"},
    {"openalex_id": "https://openalex.org/works/w2526530469"},
    {"openalex_id": "https://openalex.org/works/w2593555294"},
    {"openalex_id": "https://openalex.org/works/w2607700861"},
    {"openalex_id": "https://openalex.org/works/w273308950"},
    {"openalex_id": "https://openalex.org/works/w2804473942"},
    {"openalex_id": "https://openalex.org/works/w2887550860"},
    {"openalex_id": "https://openalex.org/works/w2952648813"},
    {"openalex_id": "https://openalex.org/works/w3016859942"},
    {"openalex_id": "https://openalex.org/works/w306678599"},
    {"openalex_id": "https://openalex.org/works/w44150910"},
    {"openalex_id": "https://openalex.org/works/w56510125"},
    {"openalex_id": "https://openalex.org/works/w595975512"},
    {"openalex_id": "https://openalex.org/works/w78345391"},
    {"openalex_id": "https://openalex.org/works/w829412593"},
]

ft = pd.DataFrame(inclusions)
ft["label_abstract_included"] = 1

# set labels and turn into single dataframe
df = utils.combine_datafiles(search, ft)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Filges_2022", df)
