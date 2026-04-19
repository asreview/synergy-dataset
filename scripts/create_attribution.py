# this script creates content for the ATTRIBUTION.md file, not the full and correct Attribition.md file.

import tomli
from pathlib import Path
import json
import pandas as pd

# adjust to the folder of datasets you want to create attribution for
DATASET_PATH = "../synergy-release-abstracts"

authors = []
citations = ""
collection_citations = []

with open("datasets.toml", "rb") as fp:
	config = tomli.load(fp)

	for dataset in config["datasets"]:
		if "active" in dataset and not dataset["active"]:
			print(f"Not active {dataset['key']}")
			continue

		dataset_path = Path(DATASET_PATH, dataset["key"])

		print(f"Processing dataset {dataset['key']}")

		with open(Path(dataset_path, "CITATION.txt"), "r", encoding="utf-8") as f:
			citations = citations + f"> [{dataset['key']}] " + f.read() + "\n"

		# collections
		collection_path = Path(dataset_path, "CITATION_collection.txt")
		if Path.is_file(collection_path):
			with open(collection_path, "r", encoding="utf-8") as f:
				collection_citations.append(f.read())

		# authors:
		with open(Path(dataset_path, "metadata_publication.json"), "r", encoding="utf-8") as f:
			data = json.load(f)
			for authorship in data["authorships"]:
				name = authorship["author"]["display_name"]
				last_name = name.split()[-1]
				orcid = authorship["author"]["orcid"]
				author_data = name
				if orcid:
					author_data = f"[{name}]({orcid})"
				# prepend lastname for sorting
				authors.append(last_name + "|" + author_data)

# Dedup, Sort and Remove last name
authors = list(set(authors))
authors.sort()
authors = [a.split("|")[1] for a in authors]

# Dedup
collection_citations = list(set(collection_citations))
collections = ""
for c in collection_citations:
	collections = collections + f" > {c}\n"



with open("attribution_auto.md", "w", encoding="utf-8") as f:
	f.write("# Attribution\n\nWe would like to thank the following authors for openly sharing the data corresponding to their systematic review:\n\n")
	f.write(", ".join(authors))
	f.write("\n\n\nReferences to datasets:\n\n")
	f.write(citations)
	f.write("\n\n\nWe thank the authors of the following collections of systematic reviews:\n\n")
	f.write(collections)
