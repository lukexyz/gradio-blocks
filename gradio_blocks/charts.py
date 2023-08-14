# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_charts.ipynb.

# %% auto 0
__all__ = ['get_sample']

# %% ../nbs/00_charts.ipynb 2
import numpy as np
import pandas as pd
import altair as alt
import math
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
pd.set_option('display.max_columns', 500)

# %% ../nbs/00_charts.ipynb 6
def get_sample(verbose=True):
    """
    Sample Sales Data, Order Info, Sales, Customer, Shipping, etc., 
    Used for Segmentation, Customer Analytics, Clustering and More. 
        - Taken from Kaggle (www.kaggle.com/datasets/kyanyoga/sample-sales-data)
    """
    data = pd.read_csv('../data/sales_data_sample.csv', encoding=('ISO-8859-1'))

    data['ORDERDATE'] = pd.to_datetime(data['ORDERDATE'])

    # Removing all the columns not revelant for this analysis to avoid confusion
    data.drop(['ORDERLINENUMBER','STATUS','PRODUCTCODE','PHONE','STATE',
           'POSTALCODE', 'TERRITORY', 'CONTACTFIRSTNAME', 'CONTACTLASTNAME'], axis=1)

    if verbose:
        print(data.shape)
        display(data.head())
    return data