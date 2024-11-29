# This script contains functionality to simplify compose scripts for new datasets

import pandas as pd

# All ID's we use to search in OpenAlex
ID_SET = ["doi", "pmid", "title", "year"]


# Sets labels and creates a unique combined dataframe of the records 
def combine_datafiles(search: pd.DataFrame, ft: pd.DataFrame, ti_ab: pd.DataFrame = pd.DataFrame()):
    
    # Set labels
    if not ti_ab.empty:
        search["label_abstract_included"] = 0
        ti_ab["label_abstract_included"] = 1
        ft["label_abstract_included"] = 1

        ti_ab["label_included"] = 0 

    search["label_included"] = 0
    ft["label_included"] = 1

    # Merge
    df = pd.concat([ft,ti_ab,search], ignore_index=True)

    # Make unique
    for id in ID_SET:
        if id not in list(df):
            df[id] = None
    df.drop_duplicates(subset=ID_SET, inplace=True, ignore_index=True)
    
    return df