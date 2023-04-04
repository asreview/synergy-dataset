from pathlib import Path
import argparse
import shutil

import json

from zipfile import ZipFile, ZIP_DEFLATED

release_lite_path = Path("..", "odss-release-lite")

SMALL_KEYS = ["id", "title", "abstract_inverted_index"]


def small_zip(src_path, dest_path):

    # read files in zip of src_path one by one and extract them

    with ZipFile(src_path, "r") as zip_full, ZipFile(
        dest_path, "w", ZIP_DEFLATED
    ) as zip_lite:

        # unzip files in zip_full one by one and load them in json format
        for fn in zip_full.namelist():

            works_lite = []

            with zip_full.open(fn) as f:
                works = json.loads(f.read())

                for work in works:
                    works_lite.append({key: work[key] for key in SMALL_KEYS})

            # write result to new zip
            zip_lite.writestr(fn, json.dumps(works_lite))


def release_lite(release_path):

    for f in release_path.iterdir():

        if f.is_dir() and not f.name.startswith("."):
            print(f.name)
            Path(release_lite_path, f.name).mkdir(exist_ok=True, parents=True)
            shutil.copyfile(f / "labels.csv", release_lite_path / f.name / "labels.csv")
            shutil.copyfile(
                f / "metadata.json", release_lite_path / f.name / "metadata.json"
            )
            shutil.copyfile(
                f / "publication_metadata.json",
                release_lite_path / f.name / "publication_metadata.json",
            )
            small_zip(f / "works.zip", release_lite_path / f.name / "works.zip")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="Build a lite release", description="Built lite release"
    )

    parser.add_argument("-r", "--release_path", default=Path("..", "odss-release"))
    args = parser.parse_args()

    release_lite(args.release_path)
