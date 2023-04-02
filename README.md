
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
) (Copy at [web.archive.org](https://web.archive.org/web/20230331020326/https://docs.openalex.org/api-entities/works/work-object) extracted on 2023-03-31) with following attributes:

Some of the notable variables are: 

| Variable                 | Type                         |   Description |
|------|-------------------------|-------------------------------|
| label_included | Bin | 1 for included records, 0 for excluded records after full text screening |
| title | String | The title of this work. |
| title | String | The title of this work. |
| title | String | The title of this work. |
| title | String | The title of this work. |
| title | String | The title of this work. |



For the full list of variables, see this persistent copy of the OpenAlex Work Object documention: https://web.archive.org/web/20230104092916/https://docs.openalex.org/api-entities/works/work-object

| Variable | Type  |  Description |
|---|---|---|
| abstract_inverted_index |  |  |
| authorships |  |  |
| best_oa_location |  |  |
| biblio |  |  |
| cited_by_api_url |  |  |
| cited_by_count |  |  |
| concepts |  |  |
| counts_by_year |  |  |
| created_date |  |  |
| display_name |  |  |
| doi |  |  |
| id |  |  |
| ids |  |  |
| is_paratext |  |  |
| is_retracted |  |  |
| locations |  |  |
| mesh |  |  |
| ngrams_url |  |  |
| open_access |  |  |
| primary_location |  |  |
| publication_date |  |  |
| publication_year |  |  |
| referenced_works |  |  |
| related_works |  |  |
| title |  |  |
| type |  |  |
| updated_date |  |  |
| author |  |  |
| author_position |  |  |
| institutions |  |  |
| raw_affiliation_string |  |  |
| is_oa |  |  |
| license |  |  |
| url |  |  |
| version |  |  |
| ngram |  |  |
| ngram_count |  |  |
| ngram_tokens |  |  |
| token_frequency |  |  |
| is_oa |  |  |
| oa_status |  |  |
| oa_url |  |  |


## Benchmark

Work in progress. 

## Attribution

We would like to thank the following authors for openly sharing the data correponding their systematic review:

[Christian Appenzeller-Herzog](https://orcid.org/0000-0001-7430-294X), [Tim Mathes](https://orcid.org/0000-0002-5304-1717), Marlies L.S. Heeres, [Karl Heinz Weiss](https://orcid.org/0000-0002-6336-9935), [Roderick H. J. Houwen](https://orcid.org/0000-0001-6124-7937), [Hannah Ewald](https://orcid.org/0000-0002-5081-1093), [Alexandra Bannach-Brown](https://orcid.org/0000-0002-3161-1395), Piotr Przybyła, James D. Thomas, Andrew S.C. Rice, Sophia Ananiadou, Jing Liao, Malcolm R. Macleod, Daniel Bos, Frank J. Wolters, Sirwan K.L. Darweesh, Meike W. Vernooij, Frank de Wolf, M. Arfan Ikram, Albert Hofman, Maria Brouwer, Alishia D. Williams, [Mitzy Kennis](https://orcid.org/0000-0002-0729-6436), Zhongfang Fu, Nicola P. Klein, Pim Cuijpers, Claudi L H Bockting, [Roger Chou](https://orcid.org/0000-0001-9889-8610), Elizabeth Clark, Mark Helfand, [Roger Chou](https://orcid.org/0000-0001-9889-8610), Kim Peterson, Mark Helfand, Anouk A. M. T. Donners, Carin M. A. Rademaker, Lisanne A. H. Bevers, [Alwin D. R. Huitema](https://orcid.org/0000-0003-1939-4639), [Roger E. G. Schutgens](https://orcid.org/0000-0002-2762-6033), Antoine C. G. Egberts, Krista Fischer, [Trevor J. Hall](https://orcid.org/0000-0002-0427-6325), [Sarah Beecham](https://orcid.org/0000-0003-1584-5447), David Bowes, David Gray, [Serena J. Counsell](https://orcid.org/0000-0002-8033-5673), [Madhan Jeyaraman](https://orcid.org/0000-0002-9045-9493), [Sathish Muthu](https://orcid.org/0000-0002-7143-4354), Parvez Ahmad Ganie, Cathalijn H. C. Leenaars, Wilhelmus Drinkenburg, Christ Nolten, Maurice Dematteis, Ruud N. J. M. A. Joosten, Matthijs G. P. Feenstra, Rob B. M. de Vries, Cathalijn H. C. Leenaars, Frans A. Stafleu, David De Jong, Maikel van Berlo, Tijmen Geurts, Tineke Coenen-de Roo, [Jan-Bas Prins](https://orcid.org/0000-0002-1831-8522), [Rosalie W. M. Kempkes](https://orcid.org/0000-0002-6232-5295), [Janneke Elzinga](https://orcid.org/0000-0002-4819-9499), [André Bleich](https://orcid.org/0000-0002-3438-0254), Rob B. M. de Vries, Franck L. B. Meijboom, [Merel Ritskes-Hoitinga](https://orcid.org/0000-0001-5315-284X), [Rosanne W. Meijboom](https://orcid.org/0000-0002-7370-0695), Helga Gardarsdottir, Antoine C. G. Egberts, [Thijs J. Giezen](https://orcid.org/0000-0002-4087-033X), [Julia M.L. Menon](https://orcid.org/0000-0002-3467-1908), F. Struijs, P Whaley, Nicholas P. Moran, Alfredo Sánchez-Tójar, [Holger Schielzeth](https://orcid.org/0000-0002-9124-2261), Klaus Reinhold, Sathish Muthu, Eswar Ramakrishnan, Sathish Muthu, Cheruku Mogulesh, Vibhu Krishnan Viswanathan, [Naveen Jeyaraman](https://orcid.org/0000-0002-4362-3326), [Satvik N. Pai](https://orcid.org/0000-0002-3621-150X), [Madhan Jeyaraman](https://orcid.org/0000-0002-9045-9493), Manish Khanna, Heidi Nelson, Linda Humphrey, Peggy Nygren, Steven M. Teutsch, Janet D. Allan, [Matthijs Oud](https://orcid.org/0000-0001-8194-3614), Arnoud Arntz, Marleen L.M. Hermens, [Rogier E. J. Verhoef](https://orcid.org/0000-0002-0876-1926), Tim Kendall, Dimitrije Radjenović, Marjan Hericko, Richard Torkar, Aleš Živkovič, Andrew A. Rooney, Abee L. Boyles, Vickie R. Walker, Milou S. C. Sep, Marijn Vellinga, R. Angela Sarabdjitsingh, Marian Joëls, [Sanne C. Smid](https://orcid.org/0000-0001-6451-202X), Daniel McNeish, [Milica Miočević](https://orcid.org/0000-0001-8487-3666), Rens van de Schoot, Eline S van der Valk, [Ozair Abawi](https://orcid.org/0000-0002-1343-6562), Mostafa Mohseni, Amir Abdelmoumen, Vincent L. Wester, [Bibian van der Voorn](https://orcid.org/0000-0003-1299-0067), Anand Krishnan V. Iyer, Erica L T van den Akker, Sanne E. Hoeks, Sjoerd A.A. van den Berg, Yolanda B. de Rijke, Tobias Stalder, Elisabeth F.C. van Rossum, [Rens van de Schoot](https://orcid.org/0000-0001-7736-2091), [Marit Sijbrandij](https://orcid.org/0000-0001-5430-9810), [Sonja D. Winter](https://orcid.org/0000-0002-2203-002X), [Sarah Depaoli](https://orcid.org/0000-0002-1277-0462), [Jeroen K. Vermunt](https://orcid.org/0000-0001-9053-9330), M.S. van der Waal, P.A.L. Seghers, P.M.J. Welsing, Lieke H. van Huis, M.H. Emmelot-Vonk, M.E. Hamaker, Eva A.M. van Dis, Suzanne C. van Veen, Muriel A. Hagenaars, [Neeltje M. Batelaan](https://orcid.org/0000-0001-6444-3781), Claudi L H Bockting, [Rinske M van den Heuvel](https://orcid.org/0000-0002-3835-4686), Pim Cuijpers, Iris M. Engelhard, Vickie R. Walker, Abee L. Boyles, Katherine E. Pelch, Stephanie Holmgren, Andrew A. Shapiro, Chad R. Blystone, Michael J. DeVito, Retha R. Newbold, Robyn B. Blain, Pamela Hartman, Kristina A. Thayer, Andrew A. Rooney, Pim N.H. Wassenaar, [Leonardo Trasande](https://orcid.org/0000-0002-1928-597X), Juliette Legler, Mila S. Welling, [Ozair Abawi](https://orcid.org/0000-0002-1343-6562), [Emma van den Eynde](https://orcid.org/0000-0002-3871-6376), [Elisabeth F.C. van Rossum](https://orcid.org/0000-0003-0120-4913), [Jutka Halberstadt](https://orcid.org/0000-0001-7563-4356), Annelies E. Brandsma, [Lotte Kleinendorst](https://orcid.org/0000-0001-9106-7478), [Erica L T van den Akker](https://orcid.org/0000-0001-5352-9328), [Bibian van der Voorn](https://orcid.org/0000-0003-1299-0067), Frank J. Wolters, Reffat A. Segufa, Sirwan K.L. Darweesh, Daniel Bos, M. Arfan Ikram, Behnam Sabayan, Albert Hofman, Sanaz Sedaghat 

Run `pyodss attribution` or see [ATTRIBUTION.md](ATTRIBUTION.md) for a complete attribution including references. 

## Citing SYNERGY dataset

If you use SYNERGY in a scientific publication, we would appreciate references to:

Biblatex entry:

```bib
@online{xxx,
  author       = {xxx},
  title        = {xxx},
  date         = {xxx},
  year         = {2023},
}
```

## Contributing

We are welcoming contributions of all kinds. Some examples are:

- Do you have an openly published systematic review dataset? Read about our ambition to develop SYNERGY+ (SYNERGY Plus), a much larger dataset with lots of new features. 
- Write an example or tutorial on how to use SYNERGY and all of its hidden capebilities. 
- Write integration to load SYNERGY into existing software like Spacy, Gensim, Tensorflow. 

## Contact

Reach out on the [Discussion forum](https://github.com/asreview/systematic-review-datasets/discussions).

