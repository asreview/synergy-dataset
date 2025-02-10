import pandas as pd
import sys

sys.path.append("../../scripts")
import utils

# Load the data
df = pd.read_excel("https://osf.io/dwxeh/download")

# Process data
df = utils.rename_columns(df, title="Title", ft_label="Included", year="Year")
df = utils.drop_duplicates(df)

# Write output
utils.write_ids_files("Pinos_Cisneros_2023", df)
