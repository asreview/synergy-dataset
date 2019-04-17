#!/usr/bin/env python

import os
import sys

import pandas as pd


def _name_from_fp(fp):
    base_name = os.path.basename(fp)
    name, _ = os.path.splitext(base_name)
    return name


def clean_drug_data(fp_in, fp_out):
    """Load drug datasets, add a new column "included_final" and write to a file.

    Aruments
    --------
    fp_in: str
        File path name to read csv file from.
    fp_out: str
        File path name to write csv file to.
    """

    name = _name_from_fp(fp_in)

    try:
        df = pd.read_csv(fp_in)
    except FileNotFoundError:
        msg = "Dataset with name {} doesn't exist".format(name)
        print(msg)
        sys.exit(192)

    df = df.assign(label_included=lambda x: (x.label2 == "I").astype(int))
    df.rename(columns={'abstracts': 'abstract'}, inplace=True)
    n_included = df['label_included'].sum()
    n_total = len(df['label_included'])
    perc_included = round(100*n_included/float(n_total), 2)
    msg = """\
*******************************************
**   Dataset  : {name: <25}**
** # Samples  : {n_total: <25}**
** # Included : {n_included: <25}**
** % Included : {perc_included: <25}**
*******************************************
"""
    print(msg.format(name=name, n_total=n_total, n_included=n_included,
                     perc_included=perc_included))
    df.to_csv(fp_out)


if __name__ == "__main__":
    num_arg = len(sys.argv)-1
    if num_arg <= 0:
        print("Error: supply file name.")
        sys.exit(192)
    elif num_arg == 1:
        dir_name = "clean_cohen_review"
        filename = "{name}.csv".format(name=_name_from_fp(sys.argv[1]))
        os.makedirs(dir_name, exist_ok=True)
        fp_out = os.path.join(dir_name, filename)
    else:
        fp_out = sys.argv[2]
    fp_in = sys.argv[1]
    clean_drug_data(fp_in, fp_out)
