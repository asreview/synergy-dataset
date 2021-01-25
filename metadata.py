import glob
import json

import pandas as pd

from asreviewcontrib.statistics import DataStatistics


def get_authors(metadata):

    all_authors = []

    for key, values in metadata.items():
        all_authors = all_authors + values['authors']

    return sorted(list(set(all_authors)))


metadata_files = glob.glob("datasets/*/*.json")

metadata = {}
for dataset_fp in metadata_files:
    with open(dataset_fp, "r", encoding="utf-8") as f:
        res = json.load(f)

        # new variables
        res["type"] = "base"

        # store results
        metadata[res["dataset_id"]] = res

# sort metadata
metadata = {k: v for k, v in sorted(metadata.items(), key=lambda item: item[0])}

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
df.drop(["type", "img_url"], axis=1, inplace=True)
df["authors"] = df["authors"].str.join("; ")

df.to_csv("index.csv", index=False)
print(df)

# # export metadata to markdown table
# df["id"] = "[" + df["dataset_id"] + "](" + df["url"] + ")"
# df["license"] = "[" + df["license"] + "](" + df["link"] + ")"
# vars_output = ["id", "topic", "n_papers", "n_included", "license"]
# s_table = df[vars_output].to_markdown(index=False)

DATASET_TEMPLATE = """
### {dataset_id}

![](images/{dataset_id}_relevant.png)

- License: {license}

"""

s_table = ""

for index, dataset in df.iterrows():
    s_dataset = DATASET_TEMPLATE.format(dataset_id=dataset["dataset_id"], license=dataset["license"])
    s_table = s_table + s_dataset

with open("README.md") as f_read:
    readme = f_read.read()

# datasets
readme_top = readme.split("<!-- BEGIN TABLE -->")[0]
readme_bottom = readme.split("<!-- END TABLE -->")[1]

readme_new = readme_top + "<!-- BEGIN TABLE -->\n\n" + s_table + "\n\n<!-- END TABLE -->" + readme_bottom

# authors
readme_top = readme_new.split("<!-- BEGIN AUTHORS -->")[0]
readme_bottom = readme_new.split("<!-- END AUTHORS -->")[1]

s_authors = ", ".join(get_authors(metadata))

readme_new = readme_top + "<!-- BEGIN AUTHORS -->\n\n" + s_authors + "\n\n<!-- END AUTHORS -->" + readme_bottom

with open("README.md", "w") as f_write:
    f_write.write(readme_new)
