# python scripts/release_works_to_labels.py

import pandas as pd
import json
from pathlib import Path
from zipfile import ZipFile
from tqdm import tqdm
import tomli


def uninvert_abstract(inverted):
    if not inverted:
        return ""

    length = max(pos for positions in inverted.values() for pos in positions) + 1
    tokens = [""] * length
    for word, positions in inverted.items():
        for pos in positions:
            tokens[pos] = word

    return " ".join(tokens).strip()


with open("datasets.toml", "rb") as fp:
    config = tomli.load(fp)

for dataset in tqdm(config.get("datasets", []), desc="Processing datasets"):
    works_to_labels = []
    key_name = dataset["key"]
    zip_path = Path("..", "synergy-release-abstracts", key_name, "works_1.zip")
    labels = pd.read_csv(Path("..", "synergy-release-abstracts", key_name, "labels.csv"))
    labels["openalex_id_split"] = labels["openalex_id"].apply(
        lambda x: x.strip().lower().split("/")[-1]
    )
    with ZipFile(zip_path, "r") as zip_file:
        for fn in zip_file.namelist():
            with zip_file.open(fn) as f:
                works = json.loads(f.read())
                for work in works:
                    openalex_id = work["id"]
                    title = work.get("title", "")
                    abstract = uninvert_abstract(
                        work.get("abstract_inverted_index", {})
                    )
                    open_access = work.get("open_access", {})
                    is_open_access = open_access.get("is_oa", False)
                    oa_status = open_access.get("oa_status", "unknown")
                    language = work.get("language", "unknown")
                    label_row = labels.loc[
                        labels["openalex_id_split"]
                        == openalex_id.strip().lower().split("/")[-1]
                    ]
                    if label_row.empty:
                        print(
                            f"Warning: No label found for {openalex_id} in {key_name}"
                        )
                    doi = (
                        work.get("doi")
                        if work.get("doi") and len(work.get("doi", "")) > 5
                        else (
                            label_row["doi"].values[0]
                            if not label_row.empty and pd.notna(label_row["doi"].values[0])
                            else ""
                        )
                    )
                    works_to_labels.append(
                        {
                            "openalex_id": openalex_id,
                            "doi": doi,
                            "pmid": label_row["pmid"].values[0]
                            if not label_row.empty
                            else "",
                            "label_included": label_row["label_included"].values[0]
                            if not label_row.empty
                            else "",
                            "label_abstract_included": label_row[
                                "label_abstract_included"
                            ].values[0]
                            if not label_row.empty
                            else "",
                            "title": title,
                            "abstract": abstract,
                            "is_open_access": is_open_access,
                            "oa_status": oa_status,
                            "language": language,
                        }
                    )
    # Save final labels.csv
    out_path = Path("..", "synergy-release-datasets", key_name)
    out_path.mkdir(parents=True, exist_ok=True)  # creates any missing folders
    df_works_to_labels = pd.DataFrame(works_to_labels)
    df_works_to_labels.to_csv(Path(out_path, "labels.csv"), index=False)
