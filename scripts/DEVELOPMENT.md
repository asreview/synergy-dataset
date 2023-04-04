
## Order of execution

```sh
python scripts/release.py
python scripts/invert_abstract_source.py
python scripts/release_insert_abstracts.py abstract_inverted_index.json -s ../synergy-release -o ../synergy-release-tmp
python scripts/invert_abstract_lens.py
python scripts/release_insert_abstracts.py abstract_inverted_index_lens.json -s ../synergy-release-tmp -o ../synergy-release-abstracts
rm -r ../synergy-release-tmp
python scripts/release_lite.py
```
