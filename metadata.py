import glob
import json


metadata_files = glob.glob("datasets/*/*.json")

metadata = {}
for dataset_fp in metadata_files:
    with open(dataset_fp, "r", encoding="utf-8") as f:
        res = json.load(f)

        # new variables
        res["type"] = "base"

        # store results
        metadata[res["dataset_id"]] = res

with open("index.json", "w", encoding="utf-8") as f_write:
    json.dump(metadata, f_write, indent=2)


# # validate
# with open("index.json", "r") as f_read:
#     print(json.load(f_read))
