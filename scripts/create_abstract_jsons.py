# python scripts/create_abstract_jsons.py

import json
import os
from collections import defaultdict

import pandas as pd
import tomli
from tqdm import tqdm

main_mapping = {}  # Top-level dict for all openalex_ids


def invert_abstract(abstract):
    """
    Build inverted abstract for a *single* abstract.
    Returns: dict(word -> [positions])
    """
    if not isinstance(abstract, str):
        return {}

    tokens = abstract.split()
    inverted = defaultdict(list)

    for pos, token in enumerate(tokens):
        inverted[token].append(pos)

    return dict(inverted)


def main():
    # Load dataset config
    with open("datasets.toml", "rb") as fp:
        config = tomli.load(fp)

    datasets = config.get("datasets", [])
    print(f"Found {len(datasets)} datasets in datasets.toml")

    for dataset in tqdm(datasets, desc="Processing datasets", unit="dataset"):
        key_name = dataset["key"]
        folder_path = os.path.join(".", "datasets", key_name)

        ids_path = os.path.join(folder_path, f"{key_name}_ids.csv")
        raw_path = os.path.join(folder_path, f"{key_name}_raw.csv")
        json_path = os.path.join(folder_path, f"{key_name}_inverted_abstracts.json")

        df_ids = pd.read_csv(ids_path)
        df_raw = pd.read_csv(raw_path)

        # Early exit if no abstract column
        if "abstract" not in df_raw.columns:
            tqdm.write(f"No abstract column for {key_name}, skipping.")
            continue

        # Limit to shorter length if mismatched
        if len(df_ids) != len(df_raw):
            tqdm.write(
                f"Mismatched row counts for {key_name}: "
                f"{len(df_ids)} IDs vs {len(df_raw)} raw entries."
            )
        n = min(len(df_ids), len(df_raw))

        mapping = {}

        for i in range(n):
            try:
                openalex_id = df_ids.loc[i, "openalex_id"]
                abstract = df_raw.loc[i, "abstract"]
                inverted = invert_abstract(abstract)

                mapping[openalex_id] = inverted  # add to dataset-specific mapping
                main_mapping[openalex_id] = inverted  # add to main mapping
            except KeyError:
                tqdm.write(f"Row mismatch in {key_name} at index {i}, stopping early.")
                break

        # Write JSON
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(mapping, f, indent=2, ensure_ascii=False)

        tqdm.write(f"Saved JSON for {key_name}")

    # Save the combined JSON
    with open("./all_inverted_abstracts.json", "w", encoding="utf-8") as f:
        json.dump(main_mapping, f, indent=2, ensure_ascii=False)

    print("\nAll done!")


if __name__ == "__main__":
    main()
