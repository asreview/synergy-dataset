# Automated Systematic Review Datasets

This project contains datasets for the [Automated Systematic
Review](https://github.com/msdslab/automated-systematic-review) project. This
repository is used to collect, preprocess and share datasets on Systematic
Review.

## Datasets

The datasets are alphabetically ordered. 

| Reference                  | Topic            | Sample Size | Inclusion | Link  |  License | 
|----------------------------|------------------|-------------|-----------|-------|----------|
| Van de Schoot et al., 2018 | PTSD             | 5783        | 0.66%     | https://osf.io/h5k2q/ |          |


## How it works

### Collecting and preprocessing data

The folder `datasets/` has a subfolder for the different Systematic Reviews
datasets. Each of these subfolders are little project. They contain code and a
`README.md`. The scripts in the different dataset folder create a subfolder
named `output/` with the result of the data collection.

### The data format

We try to standardise the format of the outputted data because we like
standards (^.^). No, the [Automated Systematic
Review](https://github.com/msdslab/automated-systematic-review) software
works better with standardised input.

The projects output CSV-formatted files and JSONlines formatted files. These
files require at least the following column names: `authors`, `title`,
`abstract`.

## Contact and contributors

Contact details can be found at the [Automated Systematic Review](#contact-and-contributors) 
project page. 