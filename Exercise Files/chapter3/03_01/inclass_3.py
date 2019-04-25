#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Exercise Files\chapter3\03_01'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# ## Python statistics essential training - 03_01_visualization
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
gapminder = pd.read_csv('Exercise Files/chapter3/03_01/gapminder.csv')



#%%
gapminder.info()


#%%
gapminder.loc[0:200:20]

#%%
gapminder[gapminder.year == 1965].plot.scatter('babies_per_woman', 'age5_surviving')

#%%
def plotyear(year):
    data = gapminder[gapminder.year == year]
    area = 5E-6 * data.population
    colors = data.region.map({'Africa': 'skyblue',
    'Europe': 'gold',
    'America': 'palegreen',
    'Asia': 'coral'})
    data.plot.scatter('babies_per_woman', 'age5_surviving', s=area, c=colors
    , linewidth=1, edgecolor='k',
    figsize=(12, 9))

#%%
plotyear(1965)

#%%
interact(plotyear, year=widgets.IntSlider(min=1950, max=2015,step=1, value=1965))

#%%
