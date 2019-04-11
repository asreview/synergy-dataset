#!/bin/bash

if [ $# -lt 1 ]; then
    echo "Supply directory to clean"
    exit 192
elif [ $# -lt 2 ]; then
    DIR_OUT="clean_cohen_review"
else
    DIR_OUT=$2
fi

echo "Output in directory $DIR_OUT"

DIR=$1

mkdir -p $DIR_OUT
for FILE in $DIR/*.csv; do
    BASE_FILE=`basename $FILE`
    FILE_OUT=$DIR_OUT/$BASE_FILE
    ./clean_cohen.py $FILE $FILE_OUT
done