#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Exercise Files\chapter2\02_03'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# ## Python statistics essential training - 02_03_pandas
#%% [markdown]
# Standard imports

#%%
import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as pp

get_ipython().run_line_magic('matplotlib', 'inline')


#%%
planets = pd.read_csv("Exercise Files/chapter2/02_03/Planets.csv")
#%%
planets

#%%
planets['Mass'] # access a pandas column

#%%
planets.Mass # access column version 2

#%%
planets.index

#%%
planets.loc(0)

#%%
planets.set_index('Planet')

#%%
planets.set_index('Planet', inplace=True)

#%%
planets.info()

#%%
len(planets)

#%%
planets.loc['MERCURY']

#%%
planets.loc['MERCURY':'EARTH']

#%%
planets.columns


#%%
planets.FirstVisited['MERCURY'] #Index ver1

#%%
planets.loc['MERCURY'].FirstVisited #Index ver2

#%%
planets.loc['MERCURY', 'FirstVisited'] #Index ver3

#%%
pd.to_datetime(planets.FirstVisited)

#%%
planets.FirstVisited = pd.to_datetime(planets.FirstVisited)

#%%
planets.FirstVisited.dt.year

#%%
2018 - planets.FirstVisited.dt.year

#%%
