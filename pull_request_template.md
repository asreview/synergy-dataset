Ensure the following changes are present in your pull request:

[] A folder datasets/{key} with {key} being the key of your added dataset.
[] A compose.py script that generates the {key}_ids.csv. This file should be located in the folder above.
[] Add a metadata entry in the datasets.toml. It should contain at least the [datasets.publication] data (doi to the published paper)

Optional:
[] The result of the compose.py script, with the openalex_id's not yet filled it (so enrich.py not yet ran)
