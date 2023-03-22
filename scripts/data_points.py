
from pyodss import Dataset, iter_datasets

# load dataset
# d = Dataset("Appenzeller-Herzog_2020")

def count_datapoints(d):

    c=0
    if isinstance(d, dict):
        for k, v in d.items():
            if k not in ["updated_date", "created_date"]:
                c += count_datapoints(v)
    elif isinstance(d, list):
        for v in d:
            c += count_datapoints(v)
    elif d is None:
        c += 0
    else:
        c += 1
    return c

total = 0
for d in iter_datasets():

    for w in d.iter_works():
        total += count_datapoints(w)

print(total)
