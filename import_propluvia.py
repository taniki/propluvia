# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import pandas as pd

# %%
years = range(2010, 2022)

years

# %%
df = pd.concat([ pd.read_csv(f'http://data.cquest.org/propluvia/propluvia_export_{y}.csv ') for y in years])

# %%
df

# %%
df.shape

# %%
df.dtypes

# %%
df.to_csv('propluvia.csv', index=False)
