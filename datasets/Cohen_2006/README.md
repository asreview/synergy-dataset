Cohen, A. M., Hersh, W. R., Peterson, K., & Yen, P. Y. (2006). **[Reducing workload in systematic review preparation using automated citation classification.][1]** _Journal of the American Medical Informatics Association : JAMIA, 13_(2), 206–219.

## Process online raw datasets
The `process_Cohen_datasets_online.ipynb` notebook processes 15 [raw datasets][2] for ASReview, and reports inclusion rates, and missing patterns and word clouds of titles and abstracts. The cleaned datasets can be found in `output/online`.

As raw datasets only have inclusion decisions, articles information (title, authors, abstract, etc.) should be retrieved from corresponding [MEDLINE][3] records by parsing the [PubMed][4] database. It takes about **3 hours** to retrieve information for all raw datasets.

The retrieval process involves a PubMed parser: 
> Achakulvisut et al., (2020). Pubmed Parser: A Python Parser for PubMed Open-Access XML Subset and MEDLINE XML Dataset XML Dataset. Journal of Open Source Software, 5(46), 1979, https://doi.org/10.21105/joss.01979

## Process local raw datasets
To avoid the time-consuming retrieval process, the `process_Cohen_datasets_local.ipynb` notebook processes 15 raw datasets in `raw`. The cleaned datasets can be found in `output/local`. There is no difference between the output of an online workflow and a local workflow.

[1]:	https://doi.org/10.1197/jamia.M1929
[2]:	https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
[3]:	https://www.nlm.nih.gov/bsd/medline.html
[4]:	https://pubmed.ncbi.nlm.nih.gov