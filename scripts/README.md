The scripts in this folder were used to develop the dataset and might be of limited use for end users. See examples for code examples.

| STEP | SCRIPT | API | INPUT | OUTPUT | DESCRIPTION |
|---|---|---|---|---|---|
| 1. | `compose.py` | `Data repositories` | RAW DATA | `_raw.csv`, `_ids.csv` | Download SR data and normalize |
| 2. | `enrich.py` | `OpenAlex` | `_ids.csv` | `_ids.csv` | Find OpenAlex ID for each record |
| 3. | `create_ids_augmented.py` | `OpenAlex` | `_ids.csv` | `_ids_augmented.csv` | Augment `_ids` with DOIs from OA, lowercase oaids, drop duplicates, and merge user abstracts |
| 4. | MANUAL | | `_ids_augmented.csv` | `_ids_augmented.csv` | Search OA IDs for inclusions |
| 5. | `enrich_ids_augmented.py` | `Lens`, `Crossref` | `_ids_augmented.csv` | `_ids_augmented.csv` | Retrieve abstracts from The Lens and Crossref, lowercase oaids, and drop duplicates |
| 6. | `release.py` | `OpenAlex` | `_ids_augmented.csv` | `works.zip`, `labels.csv` | Retrieve OA work object for records with OA ID, drop duplicates|
| 7. | `release_insert_abstracts.py` | | `_ids_augmented.csv` | `_ids_merged.csv`, `works.zip`, `labels.csv` | Merge abstracts into OA work objects, and OA abstracts into `_ids_merged.csv` |
| 8. | MANUAL | | `_ids_merged.csv` | `_ids_merged.csv`| Search for missing abstracts for inclusions |
| 9. | `release_insert_abstracts.py` | | `_ids_merged.csv` | `_ids_final.csv`, `works.zip`, `labels.csv` | Merge the manually found abstracts into OA work objects |
| 10. | `release_works_to_labels.py` | | `works.zip`, `labels.csv` | `labels.csv` | Create the dataset|
