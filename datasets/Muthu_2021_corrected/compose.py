import pandas as pd

key = "Muthu_2021_corrected"

df = pd.read_csv(f"{key}.csv", encoding="unicode-escape")

# save results to file
df.to_csv(f"{key}_raw.csv", index=False)
df.sample(frac=1, random_state=535).to_csv(f"{key}_shuffled_raw.csv", index=False)
df.reindex(
    columns=[
        "doi",
        "label_included",
    ]
).to_csv(f"{key}_ids.csv", index=False)
