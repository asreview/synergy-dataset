#!/bin/bash

FILES=(raw/*)
mkdir -p output
for FILE in ${FILES[*]}; do
    CSV_FILE=output/`basename ${FILE%.ris}`.csv
    python ./risparser.py $FILE $CSV_FILE
done

Rscript clean_schoot_lgmm_ptsd.R
