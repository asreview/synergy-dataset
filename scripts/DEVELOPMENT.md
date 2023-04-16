
## Order of execution

```sh
python scripts/release.py
python scripts/invert_abstracts_source.py
python scripts/release_insert_abstracts.py abstract_inverted_index_by_authors.json -s ../synergy-release -o ../synergy-release-tmp
python scripts/invert_abstracts_lens.py
python scripts/release_insert_abstracts.py abstract_inverted_index_lens.json -s ../synergy-release-tmp -o ../synergy-release-tmp2
python scripts/invert_abstracts_manual.py
python scripts/release_insert_abstracts.py abstract_inverted_index_manual.json -s ../synergy-release-tmp2 -o ../synergy-release-abstracts
rm -r ../synergy-release-tmp
rm -r ../synergy-release-tmp2
python scripts/release_lite.py
```
