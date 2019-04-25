#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Exercise Files\chapter3\03_03'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# ## Python statistics essential training - 03_03_histograms
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
china1965 = pd.read_csv('Exercise Files/chapter3/03_03/income-1965-china.csv')
china2015 = pd.read_csv('Exercise Files/chapter3/03_03/income-2015-china.csv')
usa1965 = pd.read_csv('Exercise Files/chapter3/03_03/income-1965-usa.csv')
usa2015 = pd.read_csv('Exercise Files/chapter3/03_03/income-2015-usa.csv')




#%%
# Points below and above whiskers are considered flyers they are not typical they may even be outliers.
# Points that are suspecious and may reflect measurment errors.
china1965.income.plot(kind='box')

#%%
china1965.plot(kind='box')

#%%
pd.DataFrame({'USA': usa1965.income, 'china': china1965.income}).boxplot()

#%%
pd.DataFrame({'USA': usa1965.log10_income, 'china': china1965.log10_income}).boxplot()

#%%
# Histogram divides the data into contigues bins and each bin, shows a rectangel with height 
# proportional to number of data points in the bin.
china1965.income.plot(kind='hist', histtype='step', bins=30)
pp.axvline(china1965.income.mean(), c='C1')
pp.axvline(china1965.income.median(), c='C1', linestyle='--')
pp.axvline(china1965.income.quantile(0.25), c='C1', linestyle=':')
pp.axvline(china1965.income.quantile(0.75), c='C1', linestyle=':')

#%%
# A desity plot is efficetely a smooth histogram
china1965.income.plot(kind='hist', histtype='step', bins=30)
china1965.income.plot.density()
pp.axis(xmin=0, xmax=3)

#%%
china1965.income.plot(kind='hist', histtype='step', bins=30, density=True)
china1965.income.plot.density()
pp.axis(xmin=0, xmax=3)
# Normalized histogram, Its just an approximation since we don't have entire histogram. 
# approximation is dependent on the scale of the smoothing. 

#%%
china1965.income.plot(kind='hist', histtype='step', bins=30, density=True)
china1965.income.plot.density(bw_method=0.5)
pp.axis(xmin=0, xmax=3)
# smoothing is choosen automatic if smoothing is not give.
# We can set smooting in density method by setting the bw_method = 0.5 or some value)


#%%
china1965.log10_income.plot.hist(histtype='step', bins=20)
usa1965.log10_income.plot.hist(histtype='step', bins=20)

levels=[0.25, 0.5, 1, 2, 4, 8, 16, 32, 64]
pp.xticks(np.log10(levels), levels);
# Observation on plot: Poorest american is richer than richest chinese in 1965.

#%%
china2015.log10_income.plot.hist(histtype='step', bins=20)
usa2015.log10_income.plot.hist(histtype='step', bins=20)

levels=[0.25, 0.5, 1, 2, 4, 8, 16, 32, 64]
pp.xticks(np.log10(levels), levels);
# Observation on plot: Chineses and americans are richer.

#%%
gapminder = pd.read_csv('Exercise Files/chapter3/03_03/gapminder.csv')
gapminder.query('country == "China" and year == 2015')

#%%
gapminder.query('country == "China" and year == 2015').population

#%%
china_pop2015 = float(gapminder.query('country == "China" and year == 2015').population)
usa_pop2015 = float(gapminder.query('country == "United States" and year == 2015').population)

#%%
china_pop2015, usa_pop2015

#%%
# Weighted histogram
china2015['weight'] = china2015/ len(china2015)
usa2015['weight'] = usa2015/ len(usa2015)

china2015.log10_income.plot.hist(histtype='step', bins=20, weights=china2015.weight)
usa2015.log10_income.plot.hist(histtype='step', bins=20, weights=usa2015.weight)

levels=[0.25, 0.5, 1, 2, 4, 8, 16, 32, 64]
pp.xticks(np.log10(levels), levels);
# lot of purchasing power of richer end of china market. corporates can tap the 