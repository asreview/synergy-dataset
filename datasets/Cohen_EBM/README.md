# Evidence-based medicine

This is a standard dataset from the medical sciences to test the performance of automated review systems such as the ASR project. This readme describes the process to obtain CSV data files that can be used by the ASR software to benchmark/test its performance.


**Reducing Workload in Systematic Review Preparation Using Automated Citation Classification**
A.M. Cohen, MD, MS, W.R. Hersh, MD, K. Peterson, MS, and Po-Yin Yen, MS
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/

## Download

``` sh
Rscript pubmed_retrieval.R
```

## Process


### Individual files:

If we want to clean some file `bash $SRC_FILE` into a file `bash $DST_FILE`:

``` bash
./clean_cohen.py $SRC_FILE $DST_FILE
```

### Complete directories:

If we have a directory `bash $SRC_DIR` with csv files:

``` bash
./clean_cohen_dir.sh $SRC_DIR $DST_DIR
```

## Copy

You will probably want to copy the processed files to some working directory.
