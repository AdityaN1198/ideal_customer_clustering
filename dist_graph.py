import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('marketing_campaign.csv',delimiter='\t')


cat_cols = []

num_cols = []
#%%
for i in df.columns:
    if df[i].dtype == 'O':
        cat_cols.append(i)
    else:
        num_cols.append(i)


for i in num_cols:
    plt.hist(df[i])