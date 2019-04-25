#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Exercise Files\chapter3\03_02'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# ## Python statistics essential training - 03_02_distributions
#%% [markdown]
# Standard imports

#%%
import numpy as np
import scipy.stats
import pandas as pd


#%%
import matplotlib
import matplotlib.pyplot as pp

from IPython import display
from ipywidgets import interact, widgets

get_ipython().run_line_magic('matplotlib', 'inline')


#%%
import re
import mailbox
import csv


#%%
china1965 = pd.read_csv('Exercise Files/chapter3/03_02/income-1965-china.csv')
china2015 = pd.read_csv('Exercise Files/chapter3/03_02/income-2015-china.csv')
usa1965 = pd.read_csv('Exercise Files/chapter3/03_02/income-1965-usa.csv')
usa2015 = pd.read_csv('Exercise Files/chapter3/03_02/income-2015-usa.csv')


#%%
china1965.info()

#%%
china1965.head()

#%%
china1965.min()

#%%
china1965.max()

#%%
china1965.mean()

#%%
china1965.var(ddof=0) # square the difference and take the average.

#%%
# A quantile is a statistics that describe a value for which a cetain percentage of the data points lie below it.
china1965.quantile((0.25, 0.75))

#%%
china1965.median() # Good chance to talk about distribution cause half points lie below and and half lie above.

#%%
# Inverse of quantile operation is 
# Finding the percentage of the poulation at which a give value lies.
x = scipy.stats.percentileofscore(china1965.income, 1.5)
print(f"The percile of 1.5 value(income) falls on {x} percentile")
# means: A person whose income is 1.5$ in china in the year 1965 is in 95.5th percentile of the distribution. 

#%%
china1965.describe()

#%%
usa1965.describe()