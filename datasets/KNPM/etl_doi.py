import pandas as pd


def process_dataset(dataset):
    df = pd.read_csv(dataset[1], usecols=['doi', 'final_included'])

    # adjust columns
    df["doi"] = df["doi"].str.extract(r"(10.\S+)")
    df['id_type'] = 'doi'

    # rename columns
    df.rename({'final_included': 'label_included', 'doi': 'id'}, axis=1, inplace=True)

    # drop missing ids
    df.dropna(subset=["id"], inplace=True)

    # drop duplicate DOIs
    df.drop_duplicates(subset=["id"], inplace=True)

    # export
    df.to_csv(f"{dataset[0]}_ids.csv", columns=['id', 'id_type', 'label_included'], index=False)


studies = [["clopidogrel", "https://osf.io/download/w69ac/"],
           ["fentanyl", "https://osf.io/download/mdcwr/"],
           ["morfine", "https://osf.io/download/wymtb/"]]

for study in studies:
    process_dataset(study)
