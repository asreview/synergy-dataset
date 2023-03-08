import requests
import pandas as pd
import numpy as np
import argparse
import re
import pyalex
import os
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile
from tqdm import tqdm

import logging

logging.basicConfig(level=logging.INFO)

tqdm.pandas()

EMAIL_POLITE_POOL = "asreview@uu.nl"

# export IEEE_KEY=xyz
API_KEY = os.getenv('IEEE_KEY')

def compare_ieee(x, y):

    x_d = str(re.search(r'arnumber\=(\d+)', x).group(1))

    return x_d in y


def get_ieee_record(x):

    x_d = str(re.search(r'arnumber\=(\d+)', x).group(1))

    r = requests.get(f"https://ieeexploreapi.ieee.org/api/v1/search/articles?article_number={x_d}&apikey={API_KEY}")
    w = pyalex.Works()["https://doi.org/" + r.json()["articles"][0]["doi"]]

    return (w["doi"], w["id"])


def get_doi_acm(row):

    if pd.isnull(row["openalex_id"]) and row["PDF Link"].startswith("http://dl.acm.org/"):
        print(row["PDF Link"])
        try:
            rh_source = requests.head(row["PDF Link"], allow_redirects=True)
            print(rh_source.url)
            w = pyalex.Works()["doi:" + rh_source.url.split("/doi/")[1]]
            return (w["doi"], w["id"])
        except Exception:
            return (None, None)
    else:
        return (row["doi"], row["openalex_id"])


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
                    logging.debug("\tNo DOI for OpenAlex record.")
            else:
                d, oa = get_ieee_record(row["PDF Link"])
                return (d, oa)

        elif res_openalex["meta"]["count"] == 0:
            logging.info("No result found on OpenAlex: " + row['Document Title'])
            d, oa = get_ieee_record(row["PDF Link"])
            return (d, oa)
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

    df_raw_in = pd.read_csv(f"{args.subset}_raw.csv")
    df_in = pd.read_csv(f"{args.subset}_ids.csv")
    df_new = pd.concat([df_raw_in, df_in], axis=1)

    # # extract DOI from ACM record
    # df_in[["doi", "openalex_id"]] = df_new.progress_apply(get_doi_acm, axis=1, result_type="expand")

    # extract the records based on ieee url
    df_new[["doi", "openalex_id"]] = df_new.apply(get_doi, axis=1, result_type="expand")

    # export the file again
    df_new[["doi", "openalex_id", "label_included"]].to_csv(f"{args.subset}_ids.csv", index=False)

