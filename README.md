
# :exclamation: This is work in progress, please do NOT use. Public release under open license will follow soon. Questions? Contact j.debruin1@uu.nl.


# SYNERGY dataset

SYNERGY is a free and open dataset on study selection in systematic reviews, comprising 111095 academic works from 25 systematic reviews. Only 1.5% of the academic works in the binary classified dataset was included in the systematic review. This makes the SYNERGY dataset an interesting dataset for the development of information retrieval algorithms, especially for sparse labels. Due to the many available variables available per record (i.e. titles, abstracts, authors, references, topics), this dataset is useful for researchers in NLP, information retrieval, network analysis and more. 

[![SYNERGY-banner.png](SYNERGY-banner.png)]()

## Get the data

The easiest way to get the SYNERGY dataset is via the `synergy-dataset` Python package.

```bash
pip install synergy-dataset
```

```python
python -m synergy get <FOLDER_TO_DOWNLOAD>
```

You can get an overview of the datasets and their properties with `synergy list` and `synergy show <DATASET_NAME>`.

> ### Slow internet connection or limited resources?
> The SYNERGY dataset is a large dataset with 50787117 datapoints. The total file size is 600Mb. It is possible to download a version of the dataset with only titles, abstracts, and labels. This dataset is smaller in size and can be rich enough for several applications. Download the dataset with `synergy get --light`


## Datasets and variables

SYNERGY is a collection of 24 systematic review datasets with in total 108853 records with 1588 total inclusions. The list of datasets and references:


|   Nr | Dataset                 | Field                         |   Records |   Included |    % |
|------|-------------------------|-------------------------------|-----------|------------|------|
|    1 | Appenzeller-Herzog_2020 | Medicine                      |      2863 |         26 |  0.9 |
|    2 | Bannach-Brown_2019      | Medicine, Computer science    |      1932 |        264 | 13.7 |
|    3 | Bos_2018                | Medicine                      |      4608 |          8 |  0.2 |
|    4 | Brouwer_2019            | Psychology, Medicine          |     38038 |         58 |  0.2 |
|    5 | Chou_2003               | Medicine                      |      1908 |         15 |  0.8 |
|    6 | Chou_2004               | Medicine                      |      1630 |          9 |  0.6 |
|    7 | Donners_2021            | Medicine                      |       258 |         14 |  5.4 |
|    8 | Hall_2012               | Computer science, Engineering |      8731 |        104 |  1.2 |
|    9 | Jeyaraman_2020          | Medicine                      |      1174 |         95 |  8.1 |
|   10 | Leenaars_2019           | Medicine, Chemistry           |      5795 |         17 |  0.3 |
|   11 | Meijboom_2022           | Medicine, Physics             |       882 |         36 |  4.1 |
|   12 | Menon_2022              | Medicine, Psychology          |       971 |         73 |  7.5 |
|   13 | Moran_2020              | Psychology, Biology           |      5203 |        107 |  2.1 |
|   14 | Muthu_2021              | Medicine, Chemistry           |      2706 |        322 | 11.9 |
|   15 | Muthu_2022              | Medicine                      |       284 |          6 |  2.1 |
|   16 | Nelson_2002             | Medicine, Physics             |       364 |         78 | 21.4 |
|   17 | Radjenovic_2013         | Computer science, Engineering |      5897 |         48 |  0.8 |
|   18 | Smid_2020               | Computer science, Mathematics |      1980 |         24 |  1.2 |
|   19 | Valk_2021               | Medicine, Mathematics         |       717 |         86 | 12   |
|   20 | van_de_Schoot_2017      | Psychology, Mathematics       |      4494 |         36 |  0.8 |
|   21 | van_der_Waal_2022       | Medicine, Political science   |      1959 |         33 |  1.7 |
|   22 | van_Dis_2020            | Psychology, Medicine          |      8791 |         59 |  0.7 |
|   23 | Welling_2022            | Medicine, Sociology           |      3678 |         58 |  1.6 |
|   24 | Wolters_2018            | Medicine                      |      3990 |         12 |  0.3 |

The each record in the dataset is an [OpenAlex Work object](https://docs.openalex.org/api-entities/works/work-object
) (extracted on 2023-XX-XX) with following attributes:

Some of the notable variables are: 

| Variable                 | Type                         |   Description |
|------|-------------------------|-------------------------------|
| title | String | String: The title of this work. |

For the full list of variables, see this persistent copy of the OpenAlex Work Object documention: https://web.archive.org/web/20230104092916/https://docs.openalex.org/api-entities/works/work-object


```
abstract_inverted_index
alternate_host_venues (deprecated)
authorships
best_oa_location
biblio
cited_by_api_url
cited_by_count
concepts
counts_by_year
created_date
display_name
doi
host_venue (deprecated)
id
ids
is_paratext
is_retracted
locations
mesh
ngrams_url
open_access
primary_location
publication_date
publication_year
referenced_works
related_works
title
type
updated_date
author
author_position
institutions
raw_affiliation_string
is_oa
license
url
version
ngram
ngram_count
ngram_tokens
token_frequency
is_oa
oa_status
oa_url
```

## Benchmark

Work in progress. 

## Attribution

We would like to thank the following authors for openly sharing the data correponding their systematic review:

[Christian Appenzeller-Herzog](https://orcid.org/0000-0001-7430-294X), [Tim Mathes](https://orcid.org/0000-0002-5304-1717), Marlies L.S. Heeres, [Karl Heinz Weiss](https://orcid.org/0000-0002-6336-9935), [Roderick H. J. Houwen](https://orcid.org/0000-0001-6124-7937), [Hannah Ewald](https://orcid.org/0000-0002-5081-1093), [Alexandra Bannach-Brown](https://orcid.org/0000-0002-3161-1395), [Piotr Przybyła](https://orcid.org/0000-0001-9043-6817), James D. Thomas, [Andrew S.C. Rice](https://orcid.org/0000-0001-9533-5636), [Sophia Ananiadou](https://orcid.org/0000-0002-4097-9191), [Jing Liao](https://orcid.org/0000-0001-7014-5377), [Malcolm R. Macleod](https://orcid.org/0000-0001-9187-9839), [Daniel Bos](https://orcid.org/0000-0001-8979-2603), [Frank J. Wolters](https://orcid.org/0000-0003-2226-4050), [Sirwan K.L. Darweesh](https://orcid.org/0000-0002-4361-4593), [Meike W. Vernooij](https://orcid.org/0000-0003-4658-2176), Frank de Wolf, [M. Arfan Ikram](https://orcid.org/0000-0003-0173-9571), [Albert Hofman](https://orcid.org/0000-0002-9865-121X), [Roger Chou](https://orcid.org/0000-0001-9889-8610), Elizabeth A. Clark, Mark Helfand, [Roger Chou](https://orcid.org/0000-0001-9889-8610), Kim Peterson, Mark Helfand, [Anouk A. M. T. Donners](https://orcid.org/0000-0002-8147-013X), Carin M. A. Rademaker, Lisanne A. H. Bevers, [Alwin D. R. Huitema](https://orcid.org/0000-0003-1939-4639), [Roger E. G. Schutgens](https://orcid.org/0000-0002-2762-6033), [Antoine C. G. Egberts](https://orcid.org/0000-0003-1758-7779), [Krista Fischer](https://orcid.org/0000-0001-7126-6613), [Trevor J. Hall](https://orcid.org/0000-0002-0427-6325), [Sarah Beecham](https://orcid.org/0000-0003-1584-5447), David Bowes, David Gray, [Serena J. Counsell](https://orcid.org/0000-0002-8033-5673), [Cathalijn H. C. Leenaars](https://orcid.org/0000-0002-8212-7632), Wilhelmus Drinkenburg, Christ Nolten, Maurice Dematteis, Ruud N. J. M. A. Joosten, Matthijs G. P. Feenstra, [Rob B. M. de Vries](https://orcid.org/0000-0002-0000-8796), [Rosanne W. Meijboom](https://orcid.org/0000-0002-7370-0695), [Helga Gardarsdottir](https://orcid.org/0000-0001-5623-9684), [Antoine C. G. Egberts](https://orcid.org/0000-0003-1758-7779), [Thijs J. Giezen](https://orcid.org/0000-0002-4087-033X), Heidi Nelson, Linda Humphrey, Peggy Nygren, Steven M. Teutsch, Janet D. Allan, Dimitrije Radjenović, [Marjan Hericko](https://orcid.org/0000-0002-1094-0085), [Richard Torkar](https://orcid.org/0000-0002-0118-8143), Aleš Živkovič, [Sanne C. Smid](https://orcid.org/0000-0001-6451-202X), [Daniel McNeish](https://orcid.org/0000-0003-1643-9408), [Milica Miočević](https://orcid.org/0000-0001-8487-3666), [Rens van de Schoot](https://orcid.org/0000-0001-7736-2091), [Eline S van der Valk](https://orcid.org/0000-0001-5134-5453), [Ozair Abawi](https://orcid.org/0000-0002-1343-6562), Mostafa Mohseni, Amir Abdelmoumen, Vincent L. Wester, [Bibian van der Voorn](https://orcid.org/0000-0003-1299-0067), [Anand Krishnan V. Iyer](https://orcid.org/0000-0002-2090-5590), [Erica L T van den Akker](https://orcid.org/0000-0001-5352-9328), [Sanne E. Hoeks](https://orcid.org/0000-0003-4022-9574), Sjoerd A.A. van den Berg, [Yolanda B. de Rijke](https://orcid.org/0000-0001-7759-4968), [Tobias Stalder](https://orcid.org/0000-0001-7558-1274), [Elisabeth F.C. van Rossum](https://orcid.org/0000-0003-0120-4913), [Rens van de Schoot](https://orcid.org/0000-0001-7736-2091), [Marit Sijbrandij](https://orcid.org/0000-0001-5430-9810), [Sonja D. Winter](https://orcid.org/0000-0002-2203-002X), [Sarah Depaoli](https://orcid.org/0000-0002-1277-0462), [Jeroen K. Vermunt](https://orcid.org/0000-0001-9053-9330), Eva A.M. van Dis, [Suzanne C. van Veen](https://orcid.org/0000-0002-5659-2557), Muriel A. Hagenaars, [Neeltje M. Batelaan](https://orcid.org/0000-0001-6444-3781), [Claudi L H Bockting](https://orcid.org/0000-0002-9220-9244), [Rinske M van den Heuvel](https://orcid.org/0000-0002-3835-4686), [Pim Cuijpers](https://orcid.org/0000-0001-5497-2743), Iris M. Engelhard, [Frank J. Wolters](https://orcid.org/0000-0003-2226-4050), Reffat A. Segufa, [Sirwan K.L. Darweesh](https://orcid.org/0000-0002-4361-4593), [Daniel Bos](https://orcid.org/0000-0001-8979-2603), [M. Arfan Ikram](https://orcid.org/0000-0003-0173-9571), [Behnam Sabayan](https://orcid.org/0000-0002-1176-9152), [Albert Hofman](https://orcid.org/0000-0002-9865-121X), [Sanaz Sedaghat](https://orcid.org/0000-0002-3244-7726)

For more credits, run `pyodss attribution`.

## Citing SYNERGY dataset

If you use SYNERGY in a scientific publication, we would appreciate references to:

Biblatex entry:

@online{xxx,
  author       = {xxx},
  title        = {xxx},
  date         = {xxx},
  year         = {2023},
}

## Contact

Reach out on the [Discussion forum](https://github.com/asreview/systematic-review-datasets/discussions).

