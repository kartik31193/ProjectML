"""
@author: kb
"""
import config
import wget
import pandas as pd

def load_dataset():
    link_to_data = config.DATAURL
    ClevelandDataSet = wget.download(link_to_data)

    heart_df = pd.read_csv(ClevelandDataSet, sep=',', header=None, names=config.COL_NAMES, na_filter=True,
                           na_values={'num_major_vessels': '?', 'thalassemia': '?'})
    heart_df['diagnosed'] = heart_df['num'].map(lambda d: 1 if d > 0 else 0)
    heart_df = heart_df.drop('num', 1)

    return heart_df
