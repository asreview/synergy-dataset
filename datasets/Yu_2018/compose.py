import requests
import pandas as pd
import numpy as np
import argparse
import re

import logging

logging.basicConfig(level=logging.INFO)

EMAIL_POLITE_POOL = "asreview@uu.nl"


def compare_ieee(x, y):

    x_d = str(re.search(r'arnumber\=(\d+)', x).group(1))

    return x_d in y


def get_doi(row):

    try:
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
        if len(res_openalex["results"]) > 1:

            logging.info("Multiple results found ({})".format(row["PDF Link"]))

            rh_source = requests.head(row["PDF Link"], allow_redirects=True)

            # get the doi
            for r in res_openalex["results"]:

                if r["doi"]:
                    rh = requests.head(r["doi"], allow_redirects=True)

                    logging.info("\tDOI {} redirects to {}".format(r["doi"], rh.url))

                    if compare_ieee(rh_source.url, rh.url):
                        logging.info("\tMatch")
                        return (r["doi"], r["id"])
                else:
                    logging.info("\tNo DOI for OpenAlex record.")

        elif res_openalex["meta"]["count"] == 0:
            logging.info("No result found on OpenAlex: " + row['Document Title'])
        else:
            w = res.json()['results'][0]
            logging.info("Result found {}".format(w["doi"]))
            return (w["doi"], w["id"])
    except Exception:
        return (None, None)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog="Compose Yu data")
    parser.add_argument("subset")
    args = parser.parse_args()

    if args.subset == "Hall_2012":
        df = pd.read_csv("https://zenodo.org/record/1162952/files/Hall.csv")
        # df = pd.read_csv("https://zenodo.org/record/1162952/files/Wahono.csv")
        # df = pd.read_csv("https://zenodo.org/record/1162952/files/Radjenovic.csv", encoding="iso-8859-1")
        # ZipFile(BytesIO(urlopen("https://zenodo.org/record/1162952/files/Kitchenham.zip").read())

    df[["doi", "openalex_id"]] = df.apply(get_doi, axis=1, result_type="expand")
    df["label_included"] = np.where(df["label"] == "yes", 1, 0)
    df[["doi", "openalex_id", "label_included"]].to_csv(f"{args.subset}_ids.csv", index=False)
