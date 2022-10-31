import requests
import pandas as pd
import numpy as np

EMAIL_POLITE_POOL = "asreview@uu.nl"


def get_doi(row):

    title_clean = row['Document Title'].replace(",", "").replace(":", "")

    params = {
        "filter": [
            "display_name.search:{}".format(title_clean),
            "publisher: 'Institute of Electrical and Electronics Engineers"
        ],
        "mailto": EMAIL_POLITE_POOL
    }
    res = requests.get("http://api.openalex.org/works", params=params)
    res.raise_for_status()

    res_openalex = res.json()

    # multiple results
    if res_openalex["meta"]["count"] > 1:

        rh_source = requests.head(row["PDF Link"], allow_redirects=True)

        # get the doi
        for r in res_openalex["results"]:

            if r["doi"]:
                rh = requests.head(r["doi"], allow_redirects=True)

                if rh_source.url.startswith(rh.url):
                    return r["doi"]

    elif res_openalex["meta"]["count"] == 0:
        return None
    else:
        return res.json()['results'][0]["doi"]

df = pd.read_csv("https://zenodo.org/record/1162952/files/Hall.csv")
df["id"] = df.apply(get_doi, axis=1).str[16:]
df["id_type"] = "doi"
df["label_included"] = np.where(df["label"] == "yes", 1, 0)
df[["PDF Link", "id", "id_type", "label_included"]].to_csv("Hall_2012_ids.csv", index=False)

df = pd.read_csv("https://zenodo.org/record/1162952/files/Wahono.csv")
df["id"] = df.apply(get_doi, axis=1).str[16:]
df["id_type"] = "doi"
df["label_included"] = np.where(df["label"] == "yes", 1, 0)
df[["PDF Link", "id", "id_type", "label_included"]].to_csv("Wahono_2015_ids.csv", index=False)

df = pd.read_csv("https://zenodo.org/record/1162952/files/Radjenovic.csv", encoding="iso-8859-1")
df["id"] = df.apply(get_doi, axis=1).str[16:]
df["id_type"] = "doi"
df["label_included"] = np.where(df["label"] == "yes", 1, 0)
df[["PDF Link", "id", "id_type", "label_included"]].to_csv("Radjenovic_2013_ids.csv", index=False)

# df = pd.read_csv("https://zenodo.org/record/1162952/files/Hall.csv")
# df["id"] = df.apply(get_doi, axis=1).str[16:]
# df["id_type"] = "doi"
# df["label_included"] = np.where(df["label"] == "yes", 1, 0)
# df[["PDF Link", "id", "id_type", "label_included"]].to_csv("Hall_2012_ids.csv", index=False)
