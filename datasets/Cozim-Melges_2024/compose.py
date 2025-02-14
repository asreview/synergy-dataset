import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Read input
utils.unzip(
    "https://static-content.springer.com/esm/art%3A10.1038%2Fs44185-023-00034-2/MediaObjects/44185_2023_34_MOESM4_ESM.zip"
)
sheets = pd.read_excel(
    "Supplementary material D - List of studies.xlsx",
    engine="openpyxl",
    sheet_name=None,
)

# Inclusions are spread out over various tabs with subjects
# I added a subset column to be able to see where records come from
bc = sheets["Bees_croplands"]
bc = utils.extract_labels(bc, "inclusion", "SELECTED")
bc["subset"] = "Bees_croplands"

wc = sheets["Wasps_crop"]
wc = utils.extract_labels(wc, "Inclusion", "SELECTED")
wc["subset"] = "Wasps_crop"

nt = sheets["Nematodes"]
nt["subset"] = "Nematodes"
ew = sheets["Earthworms"]
ew["subset"] = "Earthworms"
br = sheets["Biomass ratio"]
br["subset"] = "Biomass ratio"
nt_ew_br = pd.concat([nt, ew, br])
nt_ew_br = utils.extract_labels(nt_ew_br, "inclusion", "yes")

bc2 = sheets["birds_cropland"]
bc2["subset"] = "birds_cropland"
bc2 = utils.extract_labels(bc2, "status", "selected")

set1 = pd.concat([bc, wc, nt_ew_br, bc2])
set1 = utils.rename_columns(set1, title="Title", year="Year")

cr = sheets["Cropland-Rodent"]
cr["subset"] = "Cropland-Rodent"
rr = sheets["Rangeland-Rodent"]
rr["subset"] = "Rangeland-Rodent"
cb = sheets["Cropland-bat"]
cb["subset"] = "Cropland-bat"
sub = pd.concat([cr, rr, cb])
sub = utils.extract_labels(sub, "Inclusion", "yes")

rb = sheets["Rangeland-Bat"]
rb["subset"] = "Rangeland-Bat"
rb = utils.extract_labels(rb, "Status", "yes")

set2 = pd.concat([sub, rb])
set2 = utils.rename_columns(set2, title="Aritilce Name", year="Year")

df = pd.concat([set1, set2])

df = utils.extract_doi(df, "DOI")
df.sort_values(by=["label_included"], ascending=False, inplace=True)
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Cozim-Melges_2024", df)
