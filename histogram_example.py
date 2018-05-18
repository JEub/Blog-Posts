#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:09:30 2018

@author: james
"""

## Importing packages needed for this project
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## Setting a seed value and generating two random arrays
np.random.seed(42)
rand_array = np.random.normal(size=20)
rand_array2 = np.random.normal(size=200)

## Generating a histogram for the rand_array data
fig, ax = plt.subplots()
ax.hist(rand_array)
# Saving the plot to file in the current working directory
fig.savefig('histogram_20_blog3.png',dpi=300,transparent=True)
plt.show()


## Generating the histogram for the rand_array2 data
fig, ax = plt.subplots()
ax.hist(rand_array2,color='red')
# Saving to the current working directory
fig.savefig('histogram_200_blog3.png',dpi=300,transparent=True)
plt.show()

## Generating a DataFrame and displaying the histogram for the rand_array2 data
fig, ax = plt.subplots()
df = pd.DataFrame({'rand_array2':rand_array2})
df.plot(kind='hist',ax=ax)
# Saving to current working directory
fig.savefig('histogram_df_plot.png',dpi=300,transparent=True)
plt.show()