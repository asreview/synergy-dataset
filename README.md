# SYNERGY dataset

[![DOI](https://img.shields.io/badge/DOI-10.34894/HE6NAQ-green.svg)](https://doi.org/10.34894/HE6NAQ) ![PyPI](https://img.shields.io/pypi/v/synergy-dataset)

SYNERGY is a free and open dataset on study selection in systematic reviews, comprising 169,288 academic works from 26 systematic reviews. Only 2,834 (1.67%) of the academic works in the binary classified dataset are included in the systematic reviews. This makes the SYNERGY dataset a unique dataset for the development of information retrieval algorithms, especially for sparse labels. Due to the many variables available per record (i.e. titles, abstracts, authors, references, topics), this dataset is useful for researchers in NLP, machine learning, network analysis, and more. In total, the dataset contains 82,668,134 trainable data points. 

[![SYNERGY-banner.png](SYNERGY-banner.png)]()

## Get the data

The easiest way to get the SYNERGY dataset is via the `synergy-dataset` Python package. Install the package with:

```bash
pip install synergy-dataset
```

To download and build the SYNERGY dataset, run the following command in the command line:

```python
python -m synergy_dataset get
```

To get an overview of the datasets and their properties, use `synergy_dataset list` and `synergy_dataset show <DATASET_NAME>`.

## Datasets and variables

The SYNERGY dataset comprises the study selection of 26 systematic reviews. The dataset contains 169,288 records of which 2,834 records are manually labeled as inclusion by the authors of the systematic review. The list of systematic review and basic properties:

|   Nr | Dataset                 | Topic(s)                        |   Records |   Included |    % |
|------|-------------------------|---------------------------------|-----------|------------|------|
|    1 | Appenzeller-Herzog_2019 | Medicine                        |      2873 |         26 |  0.9 |
|    2 | Bos_2018                | Medicine                        |      4878 |         10 |  0.2 |
|    3 | Brouwer_2019            | Psychology, Medicine            |     38114 |         62 |  0.2 |
|    4 | Chou_2003               | Medicine                        |      1908 |         15 |  0.8 |
|    5 | Chou_2004               | Medicine                        |      1630 |          9 |  0.6 |
|    6 | Donners_2021            | Medicine                        |       258 |         15 |  5.8 |
|    7 | Hall_2012               | Computer science                |      8793 |        104 |  1.2 |
|    8 | Jeyaraman_2020          | Medicine                        |      1175 |         96 |  8.2 |
|    9 | Leenaars_2019           | Psychology, Chemistry, Medicine |      5812 |         17 |  0.3 |
|   10 | Leenaars_2020           | Medicine                        |      7216 |        583 |  8.1 |
|   11 | Meijboom_2021           | Medicine                        |       882 |         37 |  4.2 |
|   12 | Menon_2022              | Medicine                        |       975 |         74 |  7.6 |
|   13 | Moran_2021              | Biology, Medicine               |      5214 |        111 |  2.1 |
|   14 | Muthu_2021              | Medicine                        |      2719 |        336 | 12.4 |
|   15 | Nelson_2002             | Medicine                        |       366 |         80 | 21.9 |
|   16 | Oud_2018                | Psychology, Medicine            |       952 |         20 |  2.1 |
|   17 | Radjenovic_2013         | Computer science                |      5935 |         48 |  0.8 |
|   18 | Sep_2021                | Psychology                      |       271 |         40 | 14.8 |
|   19 | Smid_2020               | Computer science, Mathematics   |      2627 |         27 |  1   |
|   20 | van_de_Schoot_2018      | Psychology, Medicine            |      4544 |         38 |  0.8 |
|   21 | Valk_2021               | Medicine, Psychology            |       725 |         89 | 12.3 |
|   22 | van_der_Waal_2022       | Medicine                        |      1970 |         33 |  1.7 |
|   23 | van_Dis_2020            | Psychology, Medicine            |      9128 |         72 |  0.8 |
|   24 | Walker_2018             | Biology, Medicine               |     48375 |        762 |  1.6 |
|   25 | Wassenaar_2017          | Medicine, Biology, Chemistry    |      7668 |        111 |  1.4 |
|   26 | Wolters_2018            | Medicine                        |      4280 |         19 |  0.4 | 

Each record in the dataset is an [OpenAlex Work object](https://docs.openalex.org/api-entities/works/work-object
) (Copy at [web.archive.org](https://web.archive.org/web/20230331020326/https://docs.openalex.org/api-entities/works/work-object) extracted on 2023-03-31). 

Some of the notable variables are: 

| Variable                 | Type                         |   Description |
|------|-------------------------|-------------------------------|
| id | String | The OpenAlex ID for this work. |
| doi | String | The DOI identifier of the object if available |
| label_included | Bin | 1 for included records, 0 for excluded records after full text screening |
| title | String | The title of this work. |
| abstract | String | The abstract of this work. Stored as `abstract_inverted_index`, but available as plaintext abstract for machine learning purposes. |
| authorships | List | List of Authorship objects, each representing an author and their institution. |
| type | String | The type or genre of the work as defined by https://api.crossref.org/types. |
| publication_year | Integer | The year this work was published. |
| referenced_works | List | List of OpenAlex IDs for works that this work cites. |
| concepts | List | List of wikidata concept objects (or topics). |
| best_oa_location | Object | An object with the best available open access location for this work. |
| cited_by_count | Integer | The number of citations to this work at April 1st, 2023. | 


For the full list of variables, see this persistent copy of the OpenAlex Work Object documention: https://web.archive.org/web/20230104092916/https://docs.openalex.org/api-entities/works/work-object

## Benchmark

Work in progress. 

## Attribution & License

We would like to thank the following authors for openly sharing the data correponding to their systematic review:

Marlies L.S. Heeres, Marijn Vellinga, P Whaley, Mostafa Mohseni, P.M.J. Welsing, Marleen L.M. Hermens, Richard Torkar, [Holger Schielzeth](https://orcid.org/0000-0002-9124-2261), Marjan Hericko, Arnoud Arntz, Lisanne A. H. Bevers, [Christian Appenzeller-Herzog](https://orcid.org/0000-0001-7430-294X), Michael J. DeVito, Juliette Legler, [Rosalie W. M. Kempkes](https://orcid.org/0000-0002-6232-5295), Daniel Bos, Sanne C. Smid, Robyn B. Blain, Carin M. A. Rademaker, David De Jong, Antoine C. G. Egberts, Tijmen Geurts, Sathish Muthu, Suzanne C. van Veen, Janet D. Allan, Pamela Hartman, Eline S van der Valk, [Mitzy Kennis](https://orcid.org/0000-0002-0729-6436), Wilhelmus Drinkenburg, R. Angela Sarabdjitsingh, Nicola P. Klein, Helga Gardarsdottir, Anouk A. M. T. Donners, [Sonja D. Winter](https://orcid.org/0000-0002-2203-002X), Muriel A. Hagenaars, Erica L T van den Akker, Amir Abdelmoumen, Derek W. R. Gray, Kim Peterson, Eswar Ramakrishnan, Trevor J. Hall, Maurice Dematteis, [Merel Ritskes-Hoitinga](https://orcid.org/0000-0001-5315-284X), Andrew A. Shapiro, Meike W. Vernooij, Maria Brouwer, Katherine E. Pelch, Milica Miočević, Eva A.M. van Dis, [Ozair Abawi](https://orcid.org/0000-0002-1343-6562), Dimitrije Radjenović, Daniel McNeish, Peggy Nygren, Maikel van Berlo, [Alwin D. R. Huitema](https://orcid.org/0000-0003-1939-4639), Nicholas P. Moran, Chad R. Blystone, Alishia D. Williams, Ruud N. J. M. A. Joosten, Klaus Reinhold, Pim N.H. Wassenaar, Sanne E. Hoeks, Anand Krishnan V. Iyer, Sjoerd A.A. van den Berg, Tim Kendall, Lieke H. van Huis, [Rens van de Schoot](https://orcid.org/0000-0001-7736-2091), Nancy E. E. Van Loey, [Julia M.L. Menon](https://orcid.org/0000-0002-3467-1908), Cathalijn H. C. Leenaars, [Rogier E. J. Verhoef](https://orcid.org/0000-0002-0876-1926), [Sarah Depaoli](https://orcid.org/0000-0002-1277-0462), Frank de Wolf, M.E. Hamaker, [Rinske M van den Heuvel](https://orcid.org/0000-0002-3835-4686), [Leonardo Trasande](https://orcid.org/0000-0002-1928-597X), Miranda Olff, Alfredo Sánchez-Tójar, M.H. Emmelot-Vonk, Kristina A. Thayer, Steven M. Teutsch, Elisabeth F.C. van Rossum, [Bibian van der Voorn](https://orcid.org/0000-0003-1299-0067), Stephanie Holmgren, [André Bleich](https://orcid.org/0000-0002-3438-0254), M.S. van der Waal, Frank J. Wolters, [Hannah Ewald](https://orcid.org/0000-0002-5081-1093), Marian Joëls, Franck L. B. Meijboom, Yolanda B. de Rijke, Tobias Stalder, M. Arfan Ikram, P.A.L. Seghers, [Marit Sijbrandij](https://orcid.org/0000-0001-5430-9810), Vincent L. Wester, Behnam Sabayan, Tim Mathes, Parvez Ahmad Ganie, Matthijs G. P. Feenstra, Abee L. Boyles, [Matthijs Oud](https://orcid.org/0000-0001-8194-3614), Andrew A. Rooney, [Rosanne W. Meijboom](https://orcid.org/0000-0002-7370-0695), Karl Heinz Weiss, [Jan-Bas Prins](https://orcid.org/0000-0002-1831-8522), F. Struijs, David Bowes, [Neeltje M. Batelaan](https://orcid.org/0000-0001-6444-3781), Reffat A. Segufa, Serena J. Counsell, Milou S. C. Sep, Aleš Živkovič, [Madhan Jeyaraman](https://orcid.org/0000-0002-9045-9493), Sirwan K.L. Darweesh, Tineke Coenen-de Roo, Heidi Nelson, Roger Chou, Vickie R. Walker, Albert Hofman, [Roger E. G. Schutgens](https://orcid.org/0000-0002-2762-6033), Rob B. M. de Vries, Zhongfang Fu, Pim Cuijpers, Christ Nolten, Krista Fischer, [Janneke Elzinga](https://orcid.org/0000-0002-4819-9499), Roderick H. J. Houwen, Iris M. Engelhard, Linda Humphrey, Frans A. Stafleu, Simon Beecham, Mark Helfand, [Thijs J. Giezen](https://orcid.org/0000-0002-4087-033X), Retha R. Newbold, Claudi L H Bockting, Sanaz Sedaghat, Elizabeth A. Clark 

Run `synergy_dataset attribution` or see [ATTRIBUTION.md](ATTRIBUTION.md) for a complete attribution including references. 

SYNERGY dataset is released under the [CC0 1.0](LICENSE) license. SYNERGY consists of [CC0 1.0 licensed](https://docs.openalex.org/additional-help/faq#how-is-openalex-licensed) metadata works published by OpenAlex. [The Lens](https://www.lens.org/) was used for data quality checks and imputing some missing variables. 

## Citing SYNERGY dataset

If you use SYNERGY in a scientific publication, we would appreciate references to:

> De Bruin, Jonathan; Ma, Yongchao; Ferdinands, Gerbrich; Teijema, Jelle; Van de Schoot, Rens, 2023, "SYNERGY - Open machine learning dataset on study selection in systematic reviews", https://doi.org/10.34894/HE6NAQ, DataverseNL, V1

BibTeX reference:

```bib
@data{HE6NAQ_2023,
  author = {De Bruin, Jonathan and Ma, Yongchao and Ferdinands, Gerbrich and Teijema, Jelle and Van de Schoot, Rens},
  publisher = {DataverseNL},
  title = {{SYNERGY - Open machine learning dataset on study selection in systematic reviews}},
  year = {2023},
  version = {V1},
  doi = {10.34894/HE6NAQ},
  url = {https://doi.org/10.34894/HE6NAQ}
}
```

## Contributing

We are welcoming contributions of all kinds. Some examples are:

- Do you have an openly published systematic review dataset? Read about our ambition to develop [SYNERGY+ (SYNERGY Plus)](https://github.com/asreview/synergy-dataset/discussions/97), a much larger dataset with lots of new features. 
- Write an [example or tutorial](examples) on how to use SYNERGY and all of its hidden capabilities. 
- Write integration to load SYNERGY into existing software like Spacy, Gensim, Tensorflow, Docker, Hugging Face. 

## Contact

Reach out on the [Discussion forum](https://github.com/asreview/synergy-dataset/discussions).

