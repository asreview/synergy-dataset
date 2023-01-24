import numpy as np
import pandas as pd
from io import StringIO
from pathlib import Path
import requests

key = "Nagtegaal_2019"

url = "https://dataverse.harvard.edu/api/access/datafile/:persistentId?persistentId=doi:10.7910/DVN/WMGPGZ/HY6N2S"
r = requests.get(url)
file = list(r.iter_lines())

for i in range(len(file)):
    file[i] = file[i].decode("utf-8").lstrip('"').rstrip(";\r\n")
for i in [
    84,
    86,
    342,
    370,
    433,
    435,
    436,
    457,
    609,
    628,
    696,
    799,
    947,
    957,
    1030,
    1134,
    1534,
    1537,
]:
    file[i] = file[i].replace('."', '."",""') + file[i + 1].lstrip(",")
    del file[i + 1]
for i in range(len(file)):
    file[i] = file[i][:-1]
for i in range(1, len(file)):
    file[i] = file[i].replace('""""', '"')
for i in range(1, 4):
    file[i] = file[i].replace("\xa0", "")
# create a sep sign "",""
file[0] = '""' + file[0].rstrip('""')
for i in range(1, 10):
    file[i] = (
        file[i][:1]
        + '""'
        + file[i][1:-5]
        + '""'
        + file[i][-5:-4]
        + '""'
        + file[i][-4:-3]
        + '""'
        + file[i][-3:-2]
        + '""'
        + file[i][-2:-1]
        + '""'
        + file[i][-1:]
    )
for i in range(10, 100):
    file[i] = (
        file[i][:2]
        + '""'
        + file[i][2:-5]
        + '""'
        + file[i][-5:-4]
        + '""'
        + file[i][-4:-3]
        + '""'
        + file[i][-3:-2]
        + '""'
        + file[i][-2:-1]
        + '""'
        + file[i][-1:]
    )
for i in range(100, 1000):
    file[i] = (
        file[i][:3]
        + '""'
        + file[i][3:-5]
        + '""'
        + file[i][-5:-4]
        + '""'
        + file[i][-4:-3]
        + '""'
        + file[i][-3:-2]
        + '""'
        + file[i][-2:-1]
        + '""'
        + file[i][-1:]
    )
for i in range(1000, len(file)):
    file[i] = (
        file[i][:4]
        + '""'
        + file[i][4:-5]
        + '""'
        + file[i][-5:-4]
        + '""'
        + file[i][-4:-3]
        + '""'
        + file[i][-3:-2]
        + '""'
        + file[i][-2:-1]
        + '""'
        + file[i][-1:]
    )

# read the repaired dataframe
df = pd.read_csv(StringIO("\n".join(file)), sep='"",""', engine="python")
df = df.drop(["Unnamed: 0", "inclusion_code"], axis=1)

df.rename(
    columns={
        "included": "label_included",
        "abstract_included": "label_abstract_screening",
    },
    inplace=True,
)

# # adjust columns and drop missing and duplicate ids
# df['doi'] = "https://doi.org/" + df['doi'].str.extract(r"(10.\S+)")
df["doi"] = None

# save results to file
df.to_csv(f"{key}_raw.csv", index=False)

df_new = df[["doi", "label_included"]].copy()
df_new["openalex_id"] = None

df_new[["doi", "openalex_id", "label_included"]].to_csv(f"{key}_ids.csv", index=False)
