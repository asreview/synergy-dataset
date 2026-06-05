# SYNERGY+ dataset

[![DOI](https://img.shields.io/badge/DOI-10.34894/DDCVCV-green.svg)](https://doi.org/10.34894/DDCVCV) ![PyPI](https://img.shields.io/pypi/v/synergy-dataset)

<br> 

SYNERGY+ is the new version of the [SYNERGY](https://github.com/asreview/synergy-dataset) dataset. 

<br>

Just like SYNERGY, it is a free and open dataset on study selection in systematic reviews. It is a unique dataset for the development of information retrieval algorithms, especially for sparse labels. Due to the many variables available per record (i.e. titles, abstracts, authors, references, topics), this dataset is useful for researchers in NLP, machine learning, network analysis, and more.

<br>

What is new?
- Increased the number of reviews to 114!
- All 168.948 records in the dataset are open access!
- Extended cleaning done of all abstracts in the dataset. 
- Additional [metadata](https://doi.org/10.34894/DDCVCV) extracted about the reviews.

We have published a [paper]() to describe all the steps we took in creating this dataset, along with various other statistics about the dataset.

<br>

[![SYNERGY-banner.png](SYNERGY-banner.png)]()

## Get the data

The easiest way to get the SYNERGY+ dataset is via the `synergy-dataset` Python package. Install the package with:

```bash
pip install synergy-dataset
```

To download and build the SYNERGY dataset, run the following command in the command line:

```python
python -m synergy_dataset get
```

To get an overview of the datasets and their properties, use `synergy_dataset list` and `synergy_dataset show <DATASET_NAME>`.

For more available options, check out the [python package](https://github.com/asreview/synergy-dataset-py) itself

## Datasets and variables

For a nice overview of the reviews along with their topic(s), records screened, included records, and many more, please check out the [paper]() published about this.

Each record in the dataset is an [OpenAlex Work object](https://developers.openalex.org/api-reference/works
) (Copy at [web.archive.org](https://web.archive.org/web/20260604005813/https://developers.openalex.org/api-reference/works) extracted on 2026-06-04). 

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


For the full list of variables, see this persistent copy of the OpenAlex Work Object documention: https://web.archive.org/web/20260604005813/https://developers.openalex.org/api-reference/works

## Benchmark

[TODO] @Timo

## Attribution & License

We would like to thank all authors for openly sharing the data correponding to their systematic reviews.
Run `synergy_dataset attribution` or see [ATTRIBUTION.md](ATTRIBUTION.md) for a complete attribution including references. 

SYNERGY+ dataset is released under the [CC0 1.0](LICENSE) license. SYNERGY+ consists of [CC0 1.0 licensed](https://developers.openalex.org/#how-is-openalex-licensed) metadata works published by OpenAlex. [The Lens](https://www.lens.org/) was used for data quality checks and imputing some missing variables. 

## Citing SYNERGY+ dataset

If you use SYNERGY+ in a scientific publication, we would appreciate references to:

[todo]: reference to paper

BibTeX reference: [TODO]

```bib
```

## Contributing

We are welcoming contributions of all kinds. Some examples are:

- Write an [example or tutorial](examples) on how to use SYNERGY and all of its hidden capabilities. 
- Write integration to load SYNERGY into existing software like Spacy, Gensim, Tensorflow, Docker, Hugging Face. 

## Contact

Reach out on the [Discussion forum](https://github.com/asreview/synergy-dataset/discussions).

