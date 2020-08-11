# Systematic Review Datasets

This repository shows an overview of labeled datasets on Systematic Reviews. The
datasets are open datasets. The labeled data can be used for text mining and machine
learning purposes. This repository contains scripts to collect, preprocess and clean
the systematic review datasets.

If you would like to help improve ASReview, please share your dataset with us! Using your dataset about which records you have included and excluded for your systematic review, we can do research, such as simulation studies, to improve our software. This will benefit everyone who wants to use the software. If you’re interested in our research to improve the software, you can find a short report on previous simulation studies [here][54].

If you are willing to contribute to ASReview by making your dataset available, please make a Pull Request and add the
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
|[Nagtegaal et al., 2019][41] | Nudging  | 2008  | 5.03%  | [source][42] | CC0 |
|[Radjenović et al., 2013][43] | Software Fault Prediction  | 6000  | 0.80%  | [source][44] | CC-BY Attribution 4.0 International |
|[Van de Schoot et al., 2018][45] | PTSD  | 5783  | 0.66%  | [source][46] | CC-BY Attribution 4.0 International |
| [van Dis et al., 2020][47] | Anxiety-Related Disorders | 10288  | 0.70%  | [source][48] | NA |
|[Wahono, 2015][49] | Software Defect Detection  | 7002  | 0.89%  | [source][50] | CC-BY Attribution 4.0 International |


## Publishing your data
For publishing either your data and / or your AI-aided systematic review, we recommend using the Open Science frame (OSF). OSF is part of the Center for Open Science (COS), which aims at increasing openness, integrity, and reproducibility of research ([OSF][56], 2020). How to share your data using OSF: A [step-by-step guide][55].

Another platform to publish your data open access is provided by Zenodo. Zenodo is a platform which encourages scientists to share all materials (including data) that are necessary to understand the scholarly process ([Zenodo][57], 2020).

When uploading your dataset to OSF or Zenodo, make sure to provide all relevant information about the dataset, by filling out all available fields. The data to be put on Zenodo or OSF can be documented as extensively as you would like (flowcharts, explanation of certain decisions, etc.). This can include a link to the systematic review itself, if it has been published elsewhere.

### License

When sharing your dataset or a link to your already published systematic review, we recommend using a CC-BY or CC0 license for both Zenodo and OSF. By adding a Creative Commons license, everybody from individual creators to large institutions are given a standardized way to allow use of their creative work under copyright law ([Creative Commons][58], 2020).

In short, the CC-BY license means that reusers are allowed to distribute, remix, adapt, and build upon the material in any medium or format, so long as attribution is given to the creator. The license allows for commercial use. The CC0 license releases data in the public domain, allowing reuse in any form without any conditions. This can be appropriate when sharing (meta)data only. With both OSF (see step-by-step guide) and Zenodo you can easily add the license to your project after creating a project in either platform.


### Collecting and preprocessing data

The folder `datasets/` has a subfolder for the different Systematic Reviews
datasets. Each of these subfolders is little project. They contain code and a
`README.md`. The scripts in the different dataset folder create a subfolder
named `output/` with the result of the data collection.

### Format of data
After reviewing in ASReview LAB, you can export your data, which will provide a file that is in the correct format to be uploaded to the repository.
ASReview LAB accepts the file formats mentioned in the table below. More information on the format of the data to be put into ASReview LAB can be found in the [datasets][59] documentation.

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
| *Distiller*     |Not supported  |                | Supported\**  |Supported\**   |
|*EPPI-reviewer*  | Supported     |                |               |Not supported  |
| *Rayyan*        | Not supported |                | Supported     |               |
|*Robotreviewer*\***  |||||

- Supported: The data can be exported from the software and imported in ASReview LAB using this extension.
- Not supported: The exported data can not be imported in ASReview LAB using this extension.
- (empty): The data cannot be exported from the software using this extension.

\* When using Covidence it is possible to export articles in .ris formats for different citation managers,
such as Endnote, Mendeley, Refworks and Zotero. All of these are compatible with ASReview LAB.
\** When exporting from Distiller set the ``sort references by`` to ``Authors``. Then the data can be
imported in ASReview LAB.
\*** Robotreviewer does not provide exports suitable for ASReview LAB, since it supports evidence synthesis.

### Format of data without ASReview LAB
If you would like to share your data without having used ASReview LAB for the screening of your records, or because you have done the screening manually, please make sure the datafile is in the right format. Two examples can be found at the bottom of the page.

#### RIS files
[RIS files][52] are used by digital libraries, like IEEE Xplore, Scopus and ScienceDirect. Citation
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
	label_abstract_screening

### Examples
Two examples of authors who have published their systematic review data online:
- A systematic review on treatment for Wilson disease, in RIS format https://zenodo.org/record/3625931#.XvB_92ozblw
- Data from four systematic reviews on fault prediction in software engineering, in .csv format https://zenodo.org/record/1162952#.XvCCZmozblw.


## Contact and contributors

Contact details can be found at the [ASReview][53]
project page.

[1]:	https://onlinelibrary.wiley.com/doi/full/10.1111/liv.14179
[2]:	https://zenodo.org/record/3625931#.Xk5de5NKhQI
[3]:	https://systematicreviewsjournal.biomedcentral.com/articles/10.1186/s13643-019-0942-7#Comments
[4]:	https://zenodo.org/record/151190#.XQPGhYj7TD7
[5]:	https://doi.org/10.1016/j.jalz.2018.04.007
[6]:	https://osf.io/w3kbq/
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
[35]:	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1447545/
[36]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[37]:	https://ieeexplore.ieee.org/document/6035727
[38]:	https://zenodo.org/record/1162952#.XIVBE_ZFyVR
[39]:	https://doi.org/10.3390/v12010107
[40]:	https://doi.org/10.17605/OSF.IO/5S27M
[41]:	https://doi.org/10.30636/jbpa.22.71
[42]:	https://doi.org/10.7910/DVN/WMGPGZ/HY6N2S
[43]:	https://www.sciencedirect.com/science/article/abs/pii/S0950584913000426
[44]:	https://zenodo.org/record/1162952#.XIVBE_ZFyVR
[45]:	https://doi.org/10.1080/00273171.2017.1412293
[46]:	https://osf.io/h5k2q/
[47]:	https://doi.org/10.1001/jamapsychiatry.2019.3986
[48]:	https://osf.io/4d9tu/
[49]:	http://journal.ilmukomputer.org/index.php/jse/article/view/47
[50]:	https://zenodo.org/record/1162952#.XIVBE_ZFyVR
[51]:	https://github.com/asreview/asreview
[52]:	https://en.wikipedia.org/wiki/RIS_(file_format)
[53]:	https://github.com/asreview/asreview#contact-and-contributors
[54]: https://asreview.readthedocs.io/en/latest/simulation_study_results.html
[55]: https://journals.sagepub.com/doi/pdf/10.1177/2515245918757689
[56]: https://www.cos.io/our-products/osf
[57]: https://about.zenodo.org/
[58]: https://creativecommons.org/about/cclicenses/
[59]: https://asreview.readthedocs.io/en/latest/datasets.html
