import pandas as pd


fp_orginal = "datasets/Yu_2018/Hall_2012_ids.csv"
fp_update = "datasets/Yu_2018/unlabeled_ids.csv"

df_orginal = pd.read_csv(fp_orginal)
df_update = pd.read_csv(fp_update, index_col=0)

df_orginal.iloc[df_update.index, :] = df_update

df_orginal.to_csv(fp_orginal, index=False)
