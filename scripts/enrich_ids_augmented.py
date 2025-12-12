import re
import time
from collections import deque
from glob import glob
from pathlib import Path

import pandas as pd
import requests
import tomli
from bs4 import BeautifulSoup
from tqdm import tqdm

LENS_API_KEY = "[YOUR_LENS_API_KEY_HERE]"  # Replace with your actual Lens API key


class LensRateLimiter:
    def __init__(self, max_requests_per_min=10, safety_margin=9):
        self.allowed_rate = max_requests_per_min - safety_margin
        if self.allowed_rate < 1:
            self.allowed_rate = 1
        self.timestamps = deque()

    def wait(self):
        now = time.time()

        # Remove timestamps older than 1 minute
        while self.timestamps and now - self.timestamps[0] > 60:
            self.timestamps.popleft()

        # If limit reached → sleep until we leave the window
        if len(self.timestamps) >= self.allowed_rate:
            earliest = self.timestamps[0]
            sleep_time = (earliest + 60) - now
            if sleep_time > 0:
                # print(f"[RateLimiter] Sleeping {sleep_time:.2f} seconds...")
                time.sleep(sleep_time)

        self.timestamps.append(time.time())


class LensAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.limiter = LensRateLimiter(max_requests_per_min=10, safety_margin=2)

    def fetch_abstracts_batch(self, doi_list):
        self.limiter.wait()

        url = "https://api.lens.org/scholarly/search"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        payload = {
            "query": {"terms": {"ids.doi": doi_list}},
            "include": ["lens_id", "external_ids", "abstract"],
            "size": len(doi_list),
        }

        for attempt in range(2):
            try:
                response = requests.post(url, json=payload, headers=headers, timeout=30)
                response.raise_for_status()
                results = response.json().get("data", [])
                break  # Success, exit retry loop
            except requests.exceptions.RequestException as e:
                if attempt == 0:
                    if "429" in str(e):
                        print(
                            "Rate limit hit, waiting 20 additional seconds before retrying..."
                        )
                        time.sleep(20)
                    else:
                        print("Lens error:", e, "Retrying once...")
                else:
                    print("Lens error:", e, "Giving up on this batch.")
                    results = []

        output = {}
        for rec in results:
            ext_ids = rec.get("external_ids", {})
            doi = ""
            for id in ext_ids:
                if id.get("type") == "doi":
                    doi = id.get("value")
                    if doi in doi_list:
                        break

            abstract_text = rec.get("abstract", "")
            lens_id = rec.get("lens_id", "")
            output[doi] = {
                "lens_id": lens_id,
                "abstract": abstract_text,
            }

        # DOIs with no returned record
        for doi in doi_list:
            output.setdefault(doi, {"lens_id": "", "abstract": ""})

        return output


def fetch_crossref_abstract(doi):
    url = f"https://api.crossref.org/works/{doi}"
    headers = {"User-Agent": "myapp (mailto:asreview@uu.nl)"}

    for attempt in range(2):  # Try at most twice
        try:
            r = requests.get(url, headers=headers, timeout=(3, 10))

            if r.status_code == 404:
                return ""  # Return empty string for missing abstract

            r.raise_for_status()
            data = r.json().get("message", {})
            return data.get("abstract", "")

        except requests.exceptions.RequestException as e:
            if attempt == 0:
                print(f"Crossref error: {e}. Retrying once...")
            else:
                print(f"Crossref error: {e}. Giving up on DOI {doi}.")
                return ""


def word_count(text):
    if not isinstance(text, str):
        return 0
    return len(text.split())


def char_count(text):
    if not isinstance(text, str):
        return 0
    return len(text)


def normalize_abstract(abstract):
    """Normalize abstract text by removing HTML tags and extra whitespace."""
    if not isinstance(abstract, str):
        return ""

    try:
        abstract = BeautifulSoup(abstract, "lxml").get_text()
        abstract = re.sub(r"\s+", " ", abstract).strip()
    except Exception as e:
        print("Error normalizing abstract:", e, "Returning empty string")
        return ""

    return abstract


def normalize_doi(doi):
    """Strip URL prefixes and whitespace."""
    if not isinstance(doi, str):
        return None

    doi = doi.strip()

    if doi.lower().startswith("https://doi.org/"):
        doi = doi[len("https://doi.org/") :]

    return doi.strip()


def fill_missing_abstracts(df, lens_api_key, batch_size=10):
    if "abstract" not in df.columns:
        df["abstract"] = ""
    if "abstract_method" not in df.columns:
        df["abstract_method"] = ""
    if "lens_id" not in df.columns:
        df["lens_id"] = ""

    df["abstract"] = df["abstract"].astype("string")
    df["abstract_method"] = df["abstract_method"].astype("string")
    df["lens_id"] = df["lens_id"].astype("string")

    lens = LensAPI(lens_api_key)

    df["doi_normalized"] = df["doi"].apply(normalize_doi)

    mask = (~df["abstract_ok"]) & (df["doi"].str.strip().str.len() > 5)

    need = df.loc[mask, "doi_normalized"].str.strip().tolist()

    print(
        f"Total records missing abstracts: {df['abstract_ok'].value_counts().get(False, 0)}, of which {len(need)} have DOIs."
    )

    try:
        for start in tqdm(
            range(0, len(need), batch_size),
            desc="Processing batches",
            unit="batch",
        ):
            batch = need[start : start + batch_size]

            # 1) Fetch using Lens (batch)
            lens_results = lens.fetch_abstracts_batch(batch)

            for doi in batch:
                entry = lens_results.get(doi) or {"abstract": "", "lens_id": ""}
                lens_abs = normalize_abstract(entry.get("abstract", ""))
                lens_id = entry.get("lens_id", "")
                idx = df.index[df["doi_normalized"] == doi][0]  # exact match

                if word_count(lens_abs) >= 20 or char_count(lens_abs) >= 100:
                    df.at[idx, "abstract"] = lens_abs
                    df.at[idx, "abstract_ok"] = True
                    df.at[idx, "abstract_method"] = "lens"
                    df.at[idx, "lens_id"] = lens_id
                    continue

                # 2) Fallback: Crossref
                crossref_abs = normalize_abstract(fetch_crossref_abstract(doi))
                if word_count(crossref_abs) >= 20 or char_count(crossref_abs) >= 100:
                    df.at[idx, "abstract"] = crossref_abs
                    df.at[idx, "abstract_ok"] = True
                    df.at[idx, "abstract_method"] = "crossref"

        return df
    except KeyboardInterrupt as _:
        print("Stop and write results so far.")
        return df
    except Exception as e:
        print("Error during abstract enrichment:", e, "Returning partial results.")
        return df


def main():
    # Load config
    with open("datasets.toml", "rb") as fp:
        config = tomli.load(fp)

    for dataset in config["datasets"]:
        print("\n============================================")
        print("Processing dataset:", dataset["key"])
        print("============================================")

        # Find the corresponding CSV
        ds_glob = list(
            glob(str(Path("datasets", "*", f"{dataset['key']}_ids_augmented.csv")))
        )
        if not ds_glob:
            print("!! Could not find CSV for dataset:", dataset["key"])
            continue

        csv_path = Path(ds_glob[0])

        df = pd.read_csv(csv_path)
        df = fill_missing_abstracts(df, LENS_API_KEY, batch_size=1000)

        # Normalize all abstracts (ensures exisitng abstracts are cleaned too)
        df["abstract"] = df["abstract"].apply(normalize_abstract)

        # Save back, overwriting original
        df.to_csv(csv_path, index=False)

        counts = df["abstract_method"].value_counts().to_dict()

        print(
            f"--- Summary {dataset['key']} ---\n"
            f"User       {counts.get('user', 0)}\n"
            f"Lens       {counts.get('lens', 0)}\n"
            f"Crossref   {counts.get('crossref', 0)}\n"
            f"Missing    {df['abstract_ok'].value_counts().get(False, 0)}"
        )


if __name__ == "__main__":
    main()
