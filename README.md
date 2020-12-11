# Systematic Review Datasets

This repository provides an overview of labeled datasets used for Systematic Reviews. The
datasets are available under a licence and can be used for text mining and machine
learning purposes. This repository contains scripts to collect, preprocess and clean
the systematic review datasets.

If you would like to help improve ASReview, please share your dataset with us! 

Using your dataset we can do research, such as simulation studies, 
to improve our software. This will benefit everyone who wants to use the software. 
If you’re interested in our research to improve the software, 
you can find a short report on previous simulation studies [here][1].

If you are willing to contribute to ASReview by making your dataset available, 
please make a Pull Request and add the information like in the table below.

## Datasets

The datasets are alphabetically ordered.

| Reference                  | Topic            | Sample Size | Inclusion | Link  |  License |
|----------------------------|------------------|-------------|-----------|-------|----------|
| [Appenzeller-Herzog et al., 2020][2] | Wilson disease | 3425 | 0.76% | [source][3] | CC-BY Attribution 4.0 International |
| [Bannach-Brown et al., 2019][4] | Animal Model of Depression | 1993 | 14.05% | [source][5] | CC-BY Attribution 4.0 International |
| [Bos et al., 2018][6] | Dementia | 5580 | 0.18% | [source][7] | CC-BY Attribution 4.0 International |
| [Cohen et al., 2006][8] | ACEInhibitors | 2544 | 1.61% | [source][9] | Custom |
| [Cohen et al., 2006][10] | ADHD | 851 | 2.35% | [source][11] | Custom |
| [Cohen et al., 2006][12] | Antihistamines | 310 | 5.16% | [source][13] | Custom |
| [Cohen et al., 2006][14] | Atypical Antipsychotics | 1120 | 13.04% | [source][15] | Custom |
| [Cohen et al., 2006][16] | Beta Blockers | 2072 | 2.03% | [source][17] | Custom |
| [Cohen et al., 2006][18] | Calcium Channel Blockers | 1218 | 8.21% | [source][19] | Custom |
| [Cohen et al., 2006][20] | Estrogens | 368 | 21.74% | [source][21] | Custom |
| [Cohen et al., 2006][22] | NSAIDS | 393 | 10.43% | [source][23] | Custom |
| [Cohen et al., 2006][24] | Opiods | 1915 | 0.78% | [source][25] | Custom |
| [Cohen et al., 2006][26] | Oral Hypoglycemics | 503 | 27.04% | [source][27] | Custom |
| [Cohen et al., 2006][28] | Proton Pump Inhibitors | 1333 | 3.83% | [source][29] | Custom |
| [Cohen et al., 2006][30] | Skeletal Muscle Relaxants | 1643 | 0.55% | [source][31] | Custom |
| [Cohen et al., 2006][32] | Statins | 3465 | 2.45% | [source][33] | Custom |
| [Cohen et al., 2006][34] | Triptans | 671 | 3.58% | [source][35] | Custom |
| [Cohen et al., 2006][36] | Urinary Incontinence | 327 | 12.23% | [source][37] | Custom |
| [Hall et al., 2012][38] | Software Fault Prediction | 8812 | 1.18% | [source][39] | CC-BY Attribution 4.0 International |
| [Kitchenham et al., 2010][40] | Software Engineering | 1698 | 2.65% | [source][41] | CC-BY Attribution 4.0 International |
| [Kwok et al., 2020][42] | Virus Metagenomics | 2481 | 4.84% | [source][43] | CC-BY Attribution 4.0 International |
| [Nagtegaal et al., 2019][44] | Nudging | 2008 | 5.03% | [source][45] | CC0 |
| [Radjenović et al., 2013][46] | Software Fault Prediction | 5949 | 0.81% | [source][47] | CC-BY Attribution 4.0 International |
| [van de Schoot et al., 2018][48] | PTSD  | 5782 | 0.66% | [source][49] | CC-BY Attribution 4.0 International |
| [van Dis et al., 2020][50] | Anxiety-Related Disorders | 10790 | 0.68% | [source][51] | CC-By Attribution 4.0 International |
| [Wahono, 2015][52] | Software Defect Detection | 6965 | 0.89% | [source][53] | CC-BY Attribution 4.0 International |
| [Wolters et al., 2018][54] | Dementia | 4878 | 0.39% | [source][55] | CC-BY Attribution 4.0 International |


## Publishing your data
For publishing either your data and / or your AI-aided systematic review, we recommend using the Open Science frame (OSF). OSF is part of the Center for Open Science (COS), which aims at increasing openness, integrity, and reproducibility of research ([OSF][56], 2020). How to share your data using OSF: A [step-by-step guide][57].

Another platform to publish your data open access is provided by Zenodo. Zenodo is a platform which encourages scientists to share all materials (including data) that are necessary to understand the scholarly process ([Zenodo][58], 2020).

When uploading your dataset to OSF or Zenodo, make sure to provide all relevant information about the dataset, by filling out all available fields. The data to be put on Zenodo or OSF can be documented as extensively as you would like (flowcharts, explanation of certain decisions, etc.). This can include a link to the systematic review itself, if it has been published elsewhere.

### License

When sharing your dataset or a link to your already published systematic review, we recommend using a CC-BY or CC0 license for both Zenodo and OSF. By adding a Creative Commons license, everybody from individual creators to large institutions are given a standardized way to allow use of their creative work under copyright law ([Creative Commons][59], 2020).

In short, the CC-BY license means that reusers are allowed to distribute, remix, adapt, and build upon the material in any medium or format, so long as attribution is given to the creator. The license allows for commercial use. The CC0 license releases data in the public domain, allowing reuse in any form without any conditions. This can be appropriate when sharing (meta)data only. With both OSF (see step-by-step guide) and Zenodo you can easily add the license to your project after creating a project in either platform.


### Collecting and preprocessing data

The folder `datasets/` has subfolders for the different systematic reviews
datasets. In each of these subfolders, the `.ipynb` script retrieve a dataset from OSF or Zenodo, and preprocesses it by adding customized labels and marking duplicates. The script also reports the inclusion rate, and missing patterns and word clouds of titles and abstracts. After preprocessing, an ASReview-ready dataset in `.csv` format is generated in the `output/` folder.

### Format of data
After reviewing in ASReview LAB, you can export your data, which will provide a file that is in the correct format to be uploaded to the repository.
ASReview LAB accepts the file formats mentioned in the table below. More information on the format of the data to be put into ASReview LAB can be found in the [datasets][60] documentation.

|                 | **.ris** | **.tsv**   | **.csv** | **.xlsx**  |
|-----------------|----------|------------|----------|------------|
| **Citation managers**|||||
| *Endnote*       | Supported     | Not supported  |               |           |
| *Mendeley*      | Supported     |                |               |               |
| *Refworks*      | Supported     | Not supported  |               |               |
| *Zotero*        | Supported     |                | Supported     |               |
| **Search engines**  |||||  
|*CINHAL(EBSCO)*  | Not supported |                |Not supported  |               |
|*Cochrane*       | Supported     |                | Supported     |               |
| *Embase*        | Supported     |                | Supported     | Supported     |
|*Eric (Ovid)*    | Not supported |                |               |Not supported  |
|*Psychinfo*      | Not supported |                |               |Not supported  |
|*(Ovid)*         |               |                |               |               |
| *Pubmed*        | Not supported |                |Not supported  |               |
| *Scopus*        | Supported     |                |Supported      |               |
|*Web of*         | Not supported |Not supported   |               |               |
|*Science*        |               |                |               |               |
| **Systematic Review Software**|||||  
| *Abstrackr*     | Supported     |                | Supported     |               |
| *Covidence*\*   | Supported     |                | Supported     |               |
| *Distiller*     |Not supported  |                | Supported\*\*  |Supported\*\*   |
|*EPPI-reviewer*  | Supported     |                |               |Not supported  |
| *Rayyan*        | Not supported |                | Supported     |               |
|*Robotreviewer*\*\*\*  |||||

- Supported: The data can be exported from the software and imported in ASReview LAB using this extension.
- Not supported: The exported data can not be imported in ASReview LAB using this extension.
- (empty): The data cannot be exported from the software using this extension.

\* When using Covidence it is possible to export articles in .ris formats for different citation managers,
such as Endnote, Mendeley, Refworks and Zotero. All of these are compatible with ASReview LAB.
\*\* When exporting from Distiller set the `sort references by` to `Authors`. Then the data can be
imported in ASReview LAB.
\*\*\* Robotreviewer does not provide exports suitable for ASReview LAB, since it supports evidence synthesis.

### Format of data without ASReview LAB
If you would like to share your data without having used ASReview LAB for the screening of your records, or because you have done the screening manually, please make sure the datafile is in the right format. Two examples can be found at the bottom of the page.

#### RIS files
[RIS files][61] are used by digital libraries, like IEEE Xplore, Scopus and ScienceDirect. Citation
managers Mendeley and EndNote support the RIS format as well. For simulation, `T1` and `AB` are necessary tags, moreover
we use an additional RIS tag with the letters `LI` (Label included).

#### Tabular datasets
Extensions .csv, .xlsx, and .xls. CSV files should be comma separated and UTF-8 encoded. For CSV files, the simulation software accepts a set of predetermined labels in line with the ones used in RIS files:  "title" and "abstract". To indicate labelling decisions, one can use "included" or "label\_included".
The latter label called "included" is needed to indicate the final included publications in the simulations. This label should be filled with all 0’s and 1’s, where 0 means that the record is not included and 1 means included.

In general, the following column names are allowed, however except for the ones mentioned above, they will not be recognized within the simulation (based on https://pypi.org/project/RISparser/):

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

### Examples
Two examples of authors who have published their systematic review data online:
- A systematic review on treatment for Wilson disease, in RIS format https://zenodo.org/record/3625931#.XvB\_92ozblw
- Data from four systematic reviews on fault prediction in software engineering, in .csv format https://zenodo.org/record/1162952#.XvCCZmozblw.


## Contact and contributors

Contact details can be found at the [ASReview][62]
project page.

[1]:	https://asreview.readthedocs.io/en/latest/guides/simulation_study_results.html
[2]:	https://onlinelibrary.wiley.com/doi/full/10.1111/liv.14179
[3]:	https://zenodo.org/record/3625931#.Xk5de5NKhQI
[4]:	https://systematicreviewsjournal.biomedcentral.com/articles/10.1186/s13643-019-0942-7#Comments
[5]:	https://zenodo.org/record/151190#.XQPGhYj7TD7
[6]:	https://doi.org/10.1016/j.jalz.2018.04.007
[7]:	https://osf.io/w3kbq/
[8]:	https://doi.org/10.1016/j.jalz.2018.04.007
[9]:	https://osf.io/w3kbq/
[10]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[11]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[12]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[13]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[14]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[15]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[16]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[17]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[18]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[19]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[20]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[21]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[22]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[23]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[24]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[25]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[26]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[27]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[28]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[29]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[30]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[31]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[32]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[33]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[34]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[35]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[36]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[37]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[38]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[39]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[40]:	https://ieeexplore.ieee.org/document/6035727
[41]:	https://zenodo.org/record/1162952#.XIVBE_ZFyVR
[42]:	https://doi.org/10.3390/v12010107
[43]:	https://doi.org/10.17605/OSF.IO/5S27M
[44]:	https://doi.org/10.30636/jbpa.22.71
[45]:	https://doi.org/10.7910/DVN/WMGPGZ/HY6N2S
[46]:	https://www.sciencedirect.com/science/article/abs/pii/S0950584913000426
[47]:	https://zenodo.org/record/1162952#.XIVBE_ZFyVR
[48]:	https://doi.org/10.1080/00273171.2017.1412293
[49]:	https://osf.io/h5k2q/
[50]:	https://doi.org/10.1001/jamapsychiatry.2019.3986
[51]:	https://osf.io/4d9tu/
[52]:	http://journal.ilmukomputer.org/index.php?journal=jse&page=article&op=view&path%5B%5D=47
[53]:	https://zenodo.org/record/1162952#.XIVBE_ZFyVR
[54]:	https://doi.org/10.1016/j.jalz.2018.01.007
[55]:	https://osf.io/sxzjg/
[56]:	https://www.cos.io/our-products/osf
[57]:	https://journals.sagepub.com/doi/pdf/10.1177/2515245918757689
[58]:	https://about.zenodo.org/
[59]:	https://creativecommons.org/about/cclicenses/
[60]:	https://asreview.readthedocs.io/en/latest/datasets.html
[61]:	https://en.wikipedia.org/wiki/RIS_(file_format)
[62]:	https://github.com/asreview/asreview#contact
