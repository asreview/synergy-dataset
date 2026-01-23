# python scripts/release_insert_abstracts.py

import argparse
import json
import re
import shutil
import warnings
from collections import defaultdict
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from matplotlib.pyplot import stem
import pandas as pd
from bs4 import BeautifulSoup, MarkupResemblesLocatorWarning
from tqdm import tqdm

warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

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


def enrich_abstracts_in_zip(src_path, dest_path, input_path):
    # read files in zip of src_path one by one and extract them
    with (
        ZipFile(src_path, "r") as zip_full,
        ZipFile(dest_path, "w", ZIP_DEFLATED) as zip_lite,
    ):
        ids_input = pd.read_csv(input_path)
        if "adjustments" not in ids_input.columns:
            ids_input["adjustments"] = ""

        if not ids_input.empty:
            ids_input["openalex_id_lc"] = ids_input["openalex_id"].str.lower()

            # unzip files in zip_full one by one and load them in json format
            for fn in zip_full.namelist():
                works_abs = []

                with zip_full.open(fn) as f:
                    works = json.loads(f.read())

                for work in works:
                    work_id = work["id"].lower()

                    # For each work, check if its openalex_id is in ids_input
                    mask = ids_input["openalex_id_lc"] == work_id
                    if not mask.any():
                        works_abs.append(work)
                        print(
                            f"Work id {work_id} not found in {input_path.stem}, skipping"
                        )
                        continue

                    row = ids_input.loc[mask].iloc[0]

                    oa_abstract = normalize_abstract(
                        uninvert_abstract(work.get("abstract_inverted_index", None))
                    )

                    # If yes, check if abstract_ok is True, or if no abstract exists in work
                    if row["abstract_ok"] and (
                        (row["adjustments"] != "")
                        or (len(str(row["abstract"])) >= (len(oa_abstract) - 50))
                        or (("???" in oa_abstract) and ("???" not in str(row["abstract"])))
                    ):
                        # If True, replace abstract_inverted_index with inverted abstract
                        # from ids_input (user, the lens, or crossref abstract)
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
                    # the uninverted abstract from open alex in ids_input
                    else:
                        # Keep OA abstract but normalize it first, and store uninverted version
                        work["abstract_inverted_index"] = invert_abstract(oa_abstract)

                        ids_input.loc[mask, "abstract"] = oa_abstract
                        ids_input.loc[mask, "abstract_ok"] = (
                            len(oa_abstract.split()) >= 20 or len(oa_abstract) >= 100
                        )
                        ids_input.loc[mask, "abstract_method"] = "open_alex"

                    works_abs.append(work)

                # write result to new zip and update ids_input
                zip_lite.writestr(fn, json.dumps(works_abs))
            
            if "_final" not in input_path.stem:
                base, _, _ = input_path.stem.partition("_ids")
                out_stem = f"{base}_ids_final"

                ids_input.to_csv(
                    input_path.parent / f"{out_stem}{input_path.suffix}",
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
        "--input_path",
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

    dirs = sorted(
        (
            f
            for f in Path(args.source_path).iterdir()
            if f.is_dir() and not f.name.startswith(".")
        ),
        key=lambda p: p.name,
    )

    with tqdm(dirs, desc="Processing files") as pbar:
        for f in pbar:
            pbar.set_postfix(dataset=f.name)

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
                input_path=args.input_path / f.name / f"{f.name}_ids_merged.csv",
            )
