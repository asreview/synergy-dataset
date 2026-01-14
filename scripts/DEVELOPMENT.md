
## Order of execution

```sh
run_compose.ps1
python scripts/enrich.py
python scripts/create_ids_augmented.py
python scripts/enrich_ids_augmented.py
python scripts/release.py
python scripts/release_insert_abstracts.py
python scripts/release_lite.py
```
