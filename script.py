import pandas as pd
import json

x = pd.read_csv("Meta_data.csv",  ";", encoding="latin1")
x["year"] = x["year"].astype(pd.Int64Dtype()).astype(object)
del x["unknown"]

for file in x.where(x.notnull(), None).to_dict(orient="record"):
	print(file["dataset_id"])

	filename = f"datasets/{file['folder']}/{file['dataset_id']}.json"

	del file["folder"]

	with open(filename, "w") as f:
		json.dump(file, f, indent=2)
