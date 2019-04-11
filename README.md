# Automated Systematic Review Datasets

This project contains datasets for the [Automated Systematic
Review](https://github.com/msdslab/automated-systematic-review) project. This
repository is used to collect, preprocess and share datasets on Systematic
Review.

## Datasets

The datasets are alphabetically ordered. 

| Reference                  | Topic            | Sample Size | Inclusion | Link  |  License | 
|----------------------------|------------------|-------------|-----------|-------|----------|
|[Cohen et al., 2006](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/)|  ACEInhibitors |   |  | [source](https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html) |  |
|[Cohen et al., 2006](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/)|   |   |  | [source](https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html) |  |
|[Cohen et al., 2006](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/)|   |   |  | [source](https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html) |  |
|[Cohen et al., 2006](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/)|   |   |  | [source](https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html) |  |
|[Cohen et al., 2006](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/)|   |   |  | [source](https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html) |  |
|[Cohen et al., 2006](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/)|   |   |  | [source](https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html) |  |
|[Cohen et al., 2006](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/)|   |   |  | [source](https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html) |  |
|[Cohen et al., 2006](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/)|   |   |  | [source](https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html) |  |
|[Cohen et al., 2006](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/)|   |   |  | [source](https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html) |  |
|[Cohen et al., 2006](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/)|   |   |  | [source](https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html) |  |
| [Van de Schoot et al., 2018](https://doi.org/10.1080/00273171.2017.1412293) | PTSD  | 5783  | 0.66%  | [osf.io/h5k2q/](https://osf.io/h5k2q/) |  |

## How it works

### Collecting and preprocessing data

The folder `datasets/` has a subfolder for the different Systematic Reviews
datasets. Each of these subfolders are little project. They contain code and a
`README.md`. The scripts in the different dataset folder create a subfolder
named `output/` with the result of the data collection.

## Dataset formats

The [Automated Systematic Review](https://github.com/msdslab/automated-
systematic-review) software accepts several file formats like RIS and CSV. The
datasets in this project are stored in one of these formats.

### RIS files

[RIS files](https://en.wikipedia.org/wiki/RIS_(file_format)) are used by
digital libraries, like IEEE Xplore, Scopus and ScienceDirect. Citation
managers Mendeley and EndNote support the RIS format as well. For simulation,
we use an additional RIS tag with the letters `LI` (Label included).

### CSV files 

For CSV files, the software accepts a set of predetermined labels in line with
the ones used in RIS files. 

The following column names are recognized (based on https://pypi.org/project/RISparser/):

```
first_authors
secondary_authors
tertiary_authors
subsidiary_authors
abstract
author_address
accession_number
authors
custom1
custom2
custom3
custom4
custom5
custom6
custom7
custom8
caption
call_number
place_published
date
name_of_database
doi
database_provider
end_page
end_of_reference
edition
id
number
alternate_title1
alternate_title2
alternate_title3
journal_name
keywords
file_attachments1
file_attachments2
figure
language
label
note
type_of_work
notes
abstract
number_of_Volumes
original_publication
publisher
year
reviewed_item
research_notes
reprint_edition
version
issn
start_page
short_title
primary_title
secondary_title
tertiary_title
translated_author
title
translated_title
type_of_reference
unknown_tag
url
volume
publication_year
access_date
```

The custom tag is:

```
label_included
```

## Contact and contributors

Contact details can be found at the [Automated Systematic Review](https://github.com/msdslab/automated-systematic-review#contact-and-contributors) 
project page. 