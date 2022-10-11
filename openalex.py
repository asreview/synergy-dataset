import json
import glob
from pathlib import Path

import requests
import pandas as pd


EMAIL_POLITE_POOL = "asreview@uu.nl"


def openalex_work_by_id(id_list, id_type='doi', mailto=EMAIL_POLITE_POOL):
    """Get metadata from OpenAlex for a list of identifiers.
    Parameters
    ----------
    id_list : list[str]
        List of identifiers
    id_type: str
        Type of the identifier (see
        https://docs.openalex.org/about-the-data/work#ids), by default 'doi'
    mailto : str, optional
        Email address to add to the request, to end up in the polite pool
        (see https://docs.openalex.org/api#the-polite-pool), by default None
    Returns
    -------
    list[dict]
        List of OpenAlex data corresponding to the identifiers,
        not necessarily in the same order as the input.
    Raises
    ------
    requests.HTTPError
        If a request got a HTTP error response.
    """
    data = []
    page_length = 50
    url = "http://api.openalex.org/works"
    for page_start in range(0, len(id_list), page_length):
        page = id_list[page_start: page_start+page_length]
        params = {
            "filter": f"{id_type}:{'|'.join(map(str, page))}",
            "per-page": page_length,
            "mailto": mailto
        }
        res = requests.get(url, params=params)
        print(res.url)
        res.raise_for_status()
        data += res.json()['results']

    return data



id_files = Path(".").glob("datasets/*/*_ids.csv")

for fp in id_files:

    output_path = Path(*fp.parts[0:2], "openalex", fp.stem + "_metadata_openalex.json")
    if output_path.exists():
        print(f"Skip {fp}")
        continue

    output_path.parent.mkdir(parents=True, exist_ok=True)


    df = pd.read_csv(fp, index_col="id")

    works = openalex_work_by_id(df.index.to_list(), id_type="pmid")

    # if len(works) != len(ids):
    #     raise ValueError("Number of works retrieved doesn't match given list.")

    works_with_labels = []

    for i, work in enumerate(works):

        pmid = int(work["ids"]["pmid"].split("/")[-1])

        work_copy = work.copy()
        work_copy["systematic_review"] = {
            "study_selection": int(df.at[pmid, "label_included"])
        }

        works_with_labels.append(work_copy)

    # export metadata to index file
    with open(output_path, "w") as f_write:
        json.dump(works_with_labels, f_write, indent=2)

    print("Number of records original data:", len(df))
    print("Works with openalex metadata:", len(works))

