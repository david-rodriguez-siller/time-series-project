#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import geopandas as gpd
import plotly.express as px
import statsmodels.api as sm

import warnings
warnings.filterwarnings("ignore")

from scipy import stats
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from shapely.geometry import Point, Polygon
from statsmodels.tsa.api import Holt
from pandas.plotting import register_matplotlib_converters


# In[ ]:


def acquire_df():
    '''
    This function acquires the superstore csv provided it is saved to your drive
    and returns a dataframe.
    '''
    df = pd.read_csv('superstore.csv')
    return df


# In[ ]:


def fill_zip():
    '''
    This function fills in the missing zip code values from the dataset.
    the missing value comes from the City of Burlington in the state of
    Vermont. Zip code was identified and found by a google search.
    '''
    df = acquire_df()
    
    df.postal_code.fillna(value = 05401.00, inplace = True)
    return df


# In[ ]:


def column_prep():
    '''
    This function drops a couple of columns and reformats the name of
    the sub-category column to subcategory.
    '''
    
    df = acquire_df()
    
    df.rename(columns = {'sub-category':'subcategory'}, inplace = True)
    df.drop(columns = ['row_id', 'country'], inplace = True)
   
    return df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




