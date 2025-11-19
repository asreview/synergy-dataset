# python scripts/release_insert_abstracts.py all_inverted_abstracts.json

import argparse
import json
import shutil
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ABS_DICT = None


def enrich_abstracts_in_zip(src_path, dest_path):
    # read files in zip of src_path one by one and extract them

    with (
        ZipFile(src_path, "r") as zip_full,
        ZipFile(dest_path, "w", ZIP_DEFLATED) as zip_lite,
    ):
        # unzip files in zip_full one by one and load them in json format
        for fn in zip_full.namelist():
            works_abs = []

            with zip_full.open(fn) as f:
                works = json.loads(f.read())

                for work in works:
                    # insert abstract if available and if not already present
                    if (
                        ABS_DICT.get(work["id"], None)
                        and len(ABS_DICT[work["id"]]) > 20
                    ) or not work["abstract_inverted_index"]:
                        try:
                            work["abstract_inverted_index"] = ABS_DICT[work["id"]]
                        except KeyError:
                            pass
                    works_abs.append(work)

            # write result to new zip
            zip_lite.writestr(fn, json.dumps(works_abs))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Build a abstract enriched release",
        description="Built abstract enriched release",
    )
    parser.add_argument("inverted_abstracts")
    parser.add_argument(
        "-s", "--source_path", type=Path, default=Path("..", "synergy-release")
    )
    parser.add_argument(
        "-o",
        "--output_path",
        type=Path,
        default=Path("..", "synergy-release-abstracts"),
    )
    args = parser.parse_args()

    with open(args.inverted_abstracts) as f:
        ABS_DICT = json.loads(f.read())

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
                f / "works_1.zip", args.output_path / f.name / "works_1.zip"
            )
