When your pull request adds a new dataset, please check the list below. Otherwise you can remove this template.

Required:
- A folder datasets/{key} with {key} being the key of your added dataset.
- A compose.py script that generates the {key}_ids.csv. This file should be located in your new folder
- Add a metadata entry in the datasets.toml. It should contain at least the [datasets.publication] data

Optional:
- The result of the compose.py script, with the openalex_id's not yet filled it. Also located in your new folder.
