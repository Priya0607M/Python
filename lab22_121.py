# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 19:04:32 2025

@author: Priya
"""

#Write a code snippet to check the data types of each column in a DataFrame.
import pandas as pd

data = {
    'col_int': [1, 2, 3],
    'col_float': [1.5, 2.5, 3.5],
    'col_str': ['a', 'b', 'c'],

}
df = pd.DataFrame(data)

print("Data types of each column:")
print(df.dtypes)

#Write a code snippet that demonstrates how to fill missing values with the mean of a column.

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [10, np.nan, 30] 
})

print("Before imputation:")
print(df)

col_means = df.mean(numeric_only=True)
df_filled = df.fillna(col_means)

print("After filling missing values with mean:")
print(df_filled)

