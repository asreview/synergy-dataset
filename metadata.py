import glob
import json


metadata_files = glob.glob("datasets/*/*.json")

metadata = {}
for dataset_fp in metadata_files:
	with open(dataset_fp, "r") as f:
		res = json.load(f)
		metadata[res["dataset_id"]] = res

with open("index.json", "w") as f_write:
	json.dump(metadata, f_write, indent=2)
