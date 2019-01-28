# Automated Systematic Review Datasets

This project contains datasets for the [Automated Systematic
Review](https://github.com/msdslab/automated-systematic-review) project. This
repository is used to collect, preprocess and share datasets on Systematic
Review.

## Datasets

The datasets are alphabetically ordered. 

| Reference                  | Topic            | Sample Size | Inclusion | Link  |  License | 
|----------------------------|------------------|-------------|-----------|-------|----------|
|[Cohen et al., 2006](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/)|  ACEInhibitors |   |  | [www.ncbi.nlm.nih.gov/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/) |  |
|[Cohen et al., 2006](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/)|   |   |  | [www.ncbi.nlm.nih.gov/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/) |  |
|[Cohen et al., 2006](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/)|   |   |  | [www.ncbi.nlm.nih.gov/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/) |  |
|[Cohen et al., 2006](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/)|   |   |  | [www.ncbi.nlm.nih.gov/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/) |  |
|[Cohen et al., 2006](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/)|   |   |  | [www.ncbi.nlm.nih.gov/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/) |  |
|[Cohen et al., 2006](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/)|   |   |  | [www.ncbi.nlm.nih.gov/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/) |  |
|[Cohen et al., 2006](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/)|   |   |  | [www.ncbi.nlm.nih.gov/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/) |  |
|[Cohen et al., 2006](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/)|   |   |  | [www.ncbi.nlm.nih.gov/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/) |  |
|[Cohen et al., 2006](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/)|   |   |  | [www.ncbi.nlm.nih.gov/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/) |  |
|[Cohen et al., 2006](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/)|   |   |  | [www.ncbi.nlm.nih.gov/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/) |  |
| [Van de Schoot et al., 2018](https://doi.org/10.1080/00273171.2017.1412293) | PTSD  | 5783  | 0.66%  | [osf.io/h5k2q/](https://osf.io/h5k2q/) |  |


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

Contact details can be found at the [Automated Systematic Review](https://github.com/msdslab/automated-systematic-review#contact-and-contributors) 
project page. 