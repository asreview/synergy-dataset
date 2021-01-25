import os

import pandas as pd

width = 1200
height = 300
colormap = "Blues"

if __name__ == '__main__':

    dataset_ids = pd.read_csv("index.csv")["dataset_id"].values

    for dataset_id in dataset_ids:
        os.system(f"asreview wordcloud benchmark:{dataset_id} --relevant --colormap {colormap} --width {width} --height {height} -o images/{dataset_id}_relevant.png")
