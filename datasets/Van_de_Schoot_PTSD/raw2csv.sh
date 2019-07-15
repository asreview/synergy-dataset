#!/bin/bash

FILES=(raw/*)
mkdir -p csv
for FILE in ${FILES[*]}; do
    CSV_FILE=csv/`basename ${FILE%.ris}`.csv
    python ./risparser.py $FILE $CSV_FILE
done

Rscript clean_schoot_lgmm_ptsd.R
