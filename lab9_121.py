# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 16:12:59 2025

@author: Priya
"""
import pandas as pd
import numpy as np
#a.	Write a Pandas program to add, subtract, multiple and divide two Pandas 
#Series.
series1 = pd.Series([20, 40, 60, 80, 100])
series2 = pd.Series([2, 4, 6, 8, 10])

add = series1 + series2
print("Addition of Series:")
print(add)

sub = series1 - series2
print("Subtraction of Series:")
print(sub)

mul = series1 * series2
print("Multiplication of Series:")
print(mul)

div = series1 / series2
print("Division of Series:")
print(div)

#b.Write a Pandas program to convert a dictionary to a Pandas series.
dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}

print("Dictionary:")
print(dict)
series = pd.Series(dict)

print("Pandas Series:")
print(series)

#c.	Write a Pandas program to create a series from a list, numpy array and
#dict
list = [10, 20, 30, 40, 50]
series_list = pd.Series(list)
print("Series from list:")
print(series_list)

array = np.array([1.1, 2.2, 3.3, 4.4])
series_array = pd.Series(array)
print("Series from NumPy array:")
print(series_array)

dict = {'a': 100, 'b': 200, 'c': 300}
series_dict = pd.Series(dict)
print("Series from dictionary:")
print(series_dict)

#d.Write a Pandas program to stack two series vertically and horizontally 
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])

vertical_stacked = pd.concat([s1, s2], axis=0)
print("Vertically Stacked Series:")
print(vertical_stacked)
horizontal_stacked = pd.concat([s1, s2], axis=1)
print("\nHorizontally Stacked DataFrame:")
print(horizontal_stacked)