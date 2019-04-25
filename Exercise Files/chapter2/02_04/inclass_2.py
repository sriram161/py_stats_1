#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Exercise Files\chapter2\02_04'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# ## Python statistics essential training - 02_04_cleaning
#%% [markdown]
# Standard imports

#%%
import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as pp

get_ipython().run_line_magic('matplotlib', 'inline')


#%%
billboard = pd.read_csv('Exercise Files/chapter2/02_04/billboard.csv', encoding='latin-1')

#%%
billboard.head()

#%%
billboard.columns

#%%
pp.plot(billboard.loc[0, 'x1st.week':'x76th.week'])

#%%
pp.plot(range(1, 77), billboard.loc[0, 'x1st.week':'x76th.week'])

#%%
for index, row in billboard.iterrows():
    pp.plot(range(1,77), row['x1st.week':'x76th.week'], color='C0', alpha=0.1)

# plot_observation: Most songs do not last long.

#%%
# melting using 
bshort = billboard[['artist.inverted', 'track', 'time', 'date.entered', 'x1st.week', 'x2nd.week', 'x3rd.week']]


#%%
bshort.head()

#%%
bshort.columns = ['artist', 'track', 'time', 'date.entered', 'wk1', 'wk2', 'wk3']

#%%
bmelt = bshort.melt(['artist','track', 'time', 'date.entered'], ['wk1', 'wk2', 'wk3'], 'week', 'rank')

#%%
bshort.head()
#%%
bmelt.query('track =="Liar"')

#%%
bmelt['week'] = bmelt['week'].apply(lambda x: int(x[2]))

#%%
bmelt.head()

#%%
bmelt['date.entered'] = pd.to_datetime(bmelt['date.entered'])

#%%
bmelt['date.entered'] + pd.Timedelta('7 days')

#%%
bmelt['date.entered'] + pd.Timedelta('7 days') * (bmelt['week'] - 1)

#%%
bmelt.drop(['date.entered'], axis=1, inplace=True)

#%%
bmelt.query('track =="Liar"')

#%%
bfinal = bmelt[['artist', 'track', 'time', 'week', 'rank']]

#%%
bfinal.sort_values(['artist', 'track'], inplace=True)

#%%
tracks = bfinal[['artist', 'track', 'time']].drop_duplicates()

#%%
tracks.head()


#%%
tracks.index.name='id'

#%%
tracksid = tracks.reset_index()

#%%
pd.merge(tracksid, bfinal, on=['track', 'artist']).head()

#%%
