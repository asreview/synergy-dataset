# this script creates content for the ATTRIBUTION.md file, not the full and correct Attribition.md file.

import tomli
from pathlib import Path


authors = []
citations = []
collection_citations = []

with open("datasets.toml", "rb") as fp:
		config = tomli.load(fp)

	for dataset in config["datasets"]:
		if "active" in dataset and not dataset["active"]:
			print(f"Not active {dataset['key']}")
			continue

		dataset_path = Path("..", "synergy-release", dataset["key"])

		print(f"Processing dataset {dataset['key']}")

		with open(Path(dataset_path, "CITATION.txt"), "r") as f:
			citation = f.read()
			citations.add(citation)

print(citations)