# Systematic Review Datasets

This repository shows an overview of labeled datasets on Systematic Reviews. The
datasets are open datasets. The labeled data can be used for text mining and machine
learning purposes. This repository contains scripts to collect, preprocess and clean
the systematic review datasets.

We are welcoming new datasets in this overview. Make a Pull Request and add the 
information like in the table below. 

## Datasets

The datasets are alphabetically ordered. 

| Reference                  | Topic            | Sample Size | Inclusion | Link  |  License | 
|----------------------------|------------------|-------------|-----------|-------|----------|
|[Appenzeller-Herzog, 2020][1]| Wilson disease | 3453 | 0.75% | [source][2] | CC-BY Attribution 4.0 International |
|[Bannach-Brown et al., 2019][3] | Animal Model of Depression | 1993 | 14.0% | [source][4] | CC-BY Attribution 4.0 International |
|[Cohen et al., 2006][5]|  ACEInhibitors | 2544  | 1.61% | [source][6] | NA |
|[Cohen et al., 2006][7]| ADHD | 851  | 2.35% | [source][8] | NA |
|[Cohen et al., 2006][9]| Antihistamines  |  310 | 5.16% | [source][10] |NA  |
|[Cohen et al., 2006][11]| Atypical Antipsychotics  | 1120  | 13.04% | [source][12] | NA |
|[Cohen et al., 2006][13]| Beta Blockers  |  2072 | 2.03% | [source][14] |NA  |
|[Cohen et al., 2006][15]| Calcium Channel Blockers  | 1218  | 8.21% | [source][16] |NA  |
|[Cohen et al., 2006][17]| Estrogens  | 368  |21.74%  | [source][18] | NA |
|[Cohen et al., 2006][19]| NSAIDS  | 393  |10.43%  | [source][20] |NA  |
|[Cohen et al., 2006][21]| Opiods  |1915   |0.78%  | [source][22] |NA  |
|[Cohen et al., 2006][23]|Oral Hypoglycemics   | 503  |27.04%  | [source][24] | NA |
|[Cohen et al., 2006][25]|Proton Pump Inhibitors   | 1333  |3.83%  | [source][26] | NA |
|[Cohen et al., 2006][27]|Skeletal Muscle Relaxants   | 1643  |0.55%  | [source][28] | NA |
|[Cohen et al., 2006][29]|Statins   | 3465  |2.45% | [source][30] | NA |
|[Cohen et al., 2006][31]|Triptans   | 671  |3.58%  | [source][32] | NA |
|[Cohen et al., 2006][33]|Urinary Incontinence   | 327  |12.23% | [source][34] | NA |
|[Hall et al., 2012][35] | Software Fault Prediction  | 8911  | 1.17%  | [source][36] | CC-BY Attribution 4.0 International |
|[Kitchenham et al., 2010][37] | Software Engineering  | 1704  | 2.58%  | [source][38] | CC-BY Attribution 4.0 International |
|[Kwok et al., 2020][39] | Virus Metagenomics  | 2481  | 4.84%  | [source][40] | CC-BY Attribution 4.0 International | 
|[Radjenović et al., 2013][41] | Software Fault Prediction  | 6000  | 0.80%  | [source][42] | CC-BY Attribution 4.0 International |
|[Van de Schoot et al., 2018][43] | PTSD  | 5783  | 0.66%  | [source][44] | CC-BY Attribution 4.0 International |
|[Wahono, 2015][45] | Software Defect Detection  | 7002  | 0.89%  | [source][46] | CC-BY Attribution 4.0 International |

## How it works

### Collecting and preprocessing data

The folder `datasets/` has a subfolder for the different Systematic Reviews
datasets. Each of these subfolders are little project. They contain code and a
`README.md`. The scripts in the different dataset folder create a subfolder
named `output/` with the result of the data collection.

## Dataset formats

The [ASReview][47] 
software accepts several file formats like RIS and CSV. The
datasets in this project are stored in one of these formats.

### RIS files

[RIS files][48] are used by
digital libraries, like IEEE Xplore, Scopus and ScienceDirect. Citation
managers Mendeley and EndNote support the RIS format as well. For simulation,
we use an additional RIS tag with the letters `LI` (Label included).

### CSV files

For CSV files, the software accepts a set of predetermined labels in line with
the ones used in RIS files. The most commonly used ones are: "id", "authors", "date", "title", "keywords" and "abstract". To indicate labelling decisions, one can use "included" or "label\_included". 

In general, the following column names are recognized (based on https://pypi.org/project/RISparser/):

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

The custom tag is:

	label_included

## Contact and contributors

Contact details can be found at the [ASReview][49] 
project page. 

[1]:	https://onlinelibrary.wiley.com/doi/full/10.1111/liv.14179
[2]:	https://zenodo.org/record/3625931#.Xk5de5NKhQI
[3]:	https://systematicreviewsjournal.biomedcentral.com/articles/10.1186/s13643-019-0942-7#Comments
[4]:	https://zenodo.org/record/151190#.XQPGhYj7TD7
[5]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[6]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[7]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[8]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[9]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[10]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[11]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[12]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[13]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[14]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[15]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[16]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[17]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[18]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[19]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[20]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[21]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[22]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[23]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[24]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[25]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[26]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[27]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[28]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[29]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[30]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[31]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[32]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[33]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[34]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[35]:	https://ieeexplore.ieee.org/document/6035727
[36]:	https://zenodo.org/record/1162952#.XIVBE_ZFyVR
[37]:	https://www.sciencedirect.com/science/article/abs/pii/S0950584910000467
[38]:	https://zenodo.org/record/1162952#.XIVBE_ZFyVR
[39]:	https://doi.org/10.3390/v12010107
[40]:	https://doi.org/10.17605/OSF.IO/5S27M
[41]:	https://www.sciencedirect.com/science/article/abs/pii/S0950584913000426
[42]:	https://zenodo.org/record/1162952#.XIVBE_ZFyVR
[43]:	https://doi.org/10.1080/00273171.2017.1412293
[44]:	https://osf.io/h5k2q/
[45]:	http://journal.ilmukomputer.org/index.php/jse/article/view/47
[46]:	https://zenodo.org/record/1162952#.XIVBE_ZFyVR
[47]:	https://github.com/asreview/asreview
[48]:	https://en.wikipedia.org/wiki/RIS_(file_format)
[49]:	https://github.com/asreview/asreview#contact-and-contributors