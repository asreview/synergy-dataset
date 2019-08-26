#!/usr/bin/env python

import os
import subprocess
import shlex

from risparser import convert_csv_to_ris

raw_files = os.listdir("raw")
os.makedirs("csv", exist_ok=True)
for ris_file in raw_files:
    ris_fp = os.path.join("raw", ris_file)
    csv_fp = os.path.join("csv", os.path.splitext(ris_file)[0]+".csv")
    convert_csv_to_ris(ris_fp, csv_fp)

subprocess.run(shlex.split('Rscript clean_schoot_lgmm_ptsd.R'))
