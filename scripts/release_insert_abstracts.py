# python scripts/release_insert_abstracts.py

import argparse
import json
import re
import shutil
from collections import defaultdict
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

import pandas as pd
from bs4 import BeautifulSoup

ABS_DICT = None


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


def uninvert_abstract(abstract):
    """
    Rebuild abstract from inverted abstract.
    Returns: str
    """
    if not abstract:
        return ""

    length = max(pos for positions in abstract.values() for pos in positions) + 1
    tokens = [""] * length
    for word, positions in abstract.items():
        for pos in positions:
            tokens[pos] = word

    return " ".join(tokens).strip()


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


def enrich_abstracts_in_zip(src_path, dest_path, ids_augmented_path):
    # read files in zip of src_path one by one and extract them
    with (
        ZipFile(src_path, "r") as zip_full,
        ZipFile(dest_path, "w", ZIP_DEFLATED) as zip_lite,
    ):
        ids_augmented = pd.read_csv(ids_augmented_path, encoding="latin1")

        if not ids_augmented.empty:
            ids_augmented["openalex_id_lc"] = ids_augmented["openalex_id"].str.lower()

            # unzip files in zip_full one by one and load them in json format
            for fn in zip_full.namelist():
                works_abs = []

                with zip_full.open(fn) as f:
                    works = json.loads(f.read())

                for work in works:
                    work_id = work["id"].lower()

                    # For each work, check if its openalex_id is in ids_augmented
                    mask = ids_augmented["openalex_id_lc"] == work_id
                    if not mask.any():
                        works_abs.append(work)
                        print(f"Work id {work_id} not found in ids_augmented")
                        continue

                    row = ids_augmented.loc[mask].iloc[0]

                    # If yes, check if abstract_ok is True, or if no abstract exists in work
                    if row["abstract_ok"] or not bool(
                        work.get("abstract_inverted_index")
                    ):
                        # If True, replace abstract_inverted_index with inverted abstract
                        # from ids_augmented (user, the lens, or crossref abstract)
                        try:
                            work["abstract_inverted_index"] = invert_abstract(
                                row["abstract"]
                            )
                        except KeyError as e:
                            print(
                                "Failed to enrich abstract for work_id=%s in file=%s: %s",
                                work_id,
                                fn,
                                e,
                            )
                            pass

                    # If False, keep the original abstract_inverted_index, but also store
                    # the uninverted abstract from open alex in ids_augmented
                    else:
                        # Keep OA abstract but normalize it first, and store uninverted version
                        oa_abstract = normalize_abstract(uninvert_abstract(work["abstract_inverted_index"]))
                        work["abstract_inverted_index"] = invert_abstract(oa_abstract)

                        ids_augmented.loc[mask, "abstract"] = oa_abstract
                        ids_augmented.loc[mask, "abstract_ok"] = (
                            len(oa_abstract.split()) >= 20 or len(oa_abstract) >= 100
                        )
                        ids_augmented.loc[mask, "abstract_method"] = "open_alex"

                    works_abs.append(work)

                # write result to new zip and update ids_augmented
                zip_lite.writestr(fn, json.dumps(works_abs))

            ids_augmented.to_csv(
                ids_augmented_path.parent
                / f"{ids_augmented_path.stem}_updated{ids_augmented_path.suffix}",
                index=False,
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Build a abstract enriched release",
        description="Built abstract enriched release",
    )

    parser.add_argument(
        "-s", "--source_path", type=Path, default=Path("..", "synergy-release")
    )
    parser.add_argument(
        "-i",
        "--ids_augmented_path",
        type=Path,
        default=Path("..", "synergy-dataset", "datasets"),
    )
    parser.add_argument(
        "-o",
        "--output_path",
        type=Path,
        default=Path("..", "synergy-release-abstracts"),
    )
    args = parser.parse_args()

    for f in Path(args.source_path).iterdir():
        if f.is_dir() and not f.name.startswith("."):
            print(f.name)
            Path(args.output_path, f.name).mkdir(exist_ok=True, parents=True)
            shutil.copyfile(f / "labels.csv", args.output_path / f.name / "labels.csv")
            shutil.copyfile(
                f / "metadata.json", args.output_path / f.name / "metadata.json"
            )
            shutil.copyfile(
                f / "CITATION.txt", args.output_path / f.name / "CITATION.txt"
            )
            try:
                shutil.copyfile(
                    f / "CITATION_collection.txt",
                    args.output_path / f.name / "CITATION_collection.txt",
                )
            except Exception:
                pass

            shutil.copyfile(
                f / "metadata_publication.json",
                args.output_path / f.name / "metadata_publication.json",
            )
            enrich_abstracts_in_zip(
                f / "works_1.zip",
                args.output_path / f.name / "works_1.zip",
                ids_augmented_path=args.ids_augmented_path
                / f.name
                / f"{f.name}_ids_augmented.csv",
            )
