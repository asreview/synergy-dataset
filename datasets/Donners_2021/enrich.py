import pandas as pd

from time import sleep

from pyalex import Works

df_raw = pd.read_csv("Donners_2021_raw.csv")
df = pd.read_csv("Donners_2021_ids.csv")


def find_work_for_doi(doi):

    try:
        return Works()["doi:" + doi]["id"]
    except Exception as err:
        print(err)
        return None


def search_title(title):

    r, m = Works().search(title).get(return_meta=True)
    print(title)
    print("\n\n")

    if len(r) == 1:
        print("on count")
        return r[0]["doi"], r[0]["id"]
    elif len(r) > 1 and "title" in r[0] and r[0]["title"].lower() == title.lower():
        print("on title")
        return r[0]["doi"], r[0]["id"]
    elif len(r) > 1 and len(list(filter(lambda x: "relevance_score" in x and x["relevance_score"] > 5000, r))) == 1:
        print("on relevance")
        return r[0]["doi"], r[0]["id"]
    else:

        print("Multiple results", m["count"])
        return None, None

if __name__ == '__main__':

    try:
        # Update dois
        for index, row in df.iterrows():

            if pd.isnull(row["doi"]) and pd.isnull(row["openalex_id"]) and pd.notnull(df_raw.iloc[index]["title"]):
                doi, openalex_id = search_title(df_raw.iloc[index]["title"])
                print("Found new work for:", doi )
                df.loc[index, "doi"] = doi
                df.loc[index, "openalex_id"] = openalex_id
                sleep(1)

        # Update works
        for index, row in df.iterrows():

            if pd.notnull(row["doi"]) and pd.isnull(row["openalex_id"]):
                df.loc[index, "openalex_id"] = find_work_for_doi(row["doi"])
                print("Found new work for:", df.loc[index, "doi"] )
                sleep(1)
    except KeyboardInterrupt as err:
        print("Stop and write results so far.")


    df.to_csv("Donners_2021_ids.csv", index=False)
