import pandas as pd

key = "Moran_2020"

df_search = pd.read_csv("https://raw.githubusercontent.com/NPMoran/metah06_condition-dependence-of-boldness_OSF/master/screening_ref_data_rayyan.csv")
df_inclusions = pd.read_csv("https://raw.githubusercontent.com/NPMoran/metah06_condition-dependence-of-boldness_OSF/master/screening_ref_data_rayyan_final.csv")

# set labels and turn into single dataframe
df_inclusions["label_included"] = 1
df_search["label_included"] = 0
df = pd.concat([df_inclusions, df_search], ignore_index=True)

# save results to file
df.to_csv(f"{key}_raw.csv", index=False)

df["doi"] = "https://doi.org/" + df["url"].str.extract(r"(10.\S+)")

df_new = df[["doi", "label_included"]].copy()
df_new["openalex_id"] = None

df_new[["doi", "openalex_id", "label_included"]].to_csv(f"{key}_ids.csv", index=False)
