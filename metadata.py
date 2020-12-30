import glob
import json

import pandas as pd

from asreviewcontrib.statistics import DataStatistics

metadata_files = glob.glob("datasets/*/*.json")

metadata = {}
for dataset_fp in metadata_files:
    with open(dataset_fp, "r", encoding="utf-8") as f:
        res = json.load(f)

        # new variables
        res["type"] = "base"

        # store results
        metadata[res["dataset_id"]] = res

# export metadata to index file
with open("index.json", "w", encoding="utf-8") as f_write:
    json.dump(metadata, f_write, indent=2)

# # test
# with open("index.json", "r") as f_read:
#     print(json.load(f_read))

# export metadata to file
result = []

for _, x in metadata.items():

    try:
        stats = DataStatistics(x["url"]).to_dict()
    except Exception as err:
        print(x)
        raise err

    x_copy = x.copy()
    x_copy.update(stats)

    result.append(x_copy)

df = pd.DataFrame(result)
# df.drop(["type"], axis=1, inplace=True)

df.to_csv("index.csv", index=False)
print(df)

# export metadata to markdown table
vars_output = ["dataset_id", "url", "license", "topic", "sample_size", "final_inclusions"]
s_table = df[vars_output].to_markdown(index=False)

with open("README.md") as f_read:
    readme = f_read.read()

readme_top = readme.split("<!-- BEGIN TABLE -->")[0]
readme_bottom = readme.split("<!-- END TABLE -->")[1]

readme_new = readme_top + "<!-- BEGIN TABLE -->\n\n" + s_table + "\n\n<!-- END TABLE -->\n\n" + readme_bottom

with open("README.md", "w") as f_write:
    f_write.write(readme_new)
