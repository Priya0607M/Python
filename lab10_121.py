# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 16:03:41 2025

@author: Priya
"""

#1.Write a Python program to draw a line with suitable label in the x axis
#, y axis and a title.

import matplotlib.pyplot as plt 
x = [1,2,1] 
y = [3,4,3] 
plt.plot(x, y)
plt.title("Line Chart")
plt.legend(["Line"])
plt.show()

#2.Write a Python program to plot two or more lines on same plot with 
#suitable legends of each line.

import matplotlib.pyplot as plt
x1 = [0,1,2,3,4]
y1 = [0,2,4,6,8]
x2 = [0,1,2,3,4]
y2 = [0,3,6,9,12]
x3 = [0,1,2,3,4]
y3 = [0,4,8,16,24]
plt.plot(x1, y1, label='Line 1', color='black', linestyle='-', marker='o')
plt.plot(x2, y2, label='Line 2', color='blue', linestyle='--', marker='s')
plt.plot(x3, y3, label='Line 3', color='green', linestyle=':', marker='^')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.legend()
plt.show()

#3.Write a Python programming to display a bar chart of the popularity of 
#programming Languages.
#Sample data:
#Programming languages: Java, Python, PHP, JavaScript, C#, C++
#Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

import matplotlib.pyplot as plt  
x = ['Java','Python','PHP','Javascript','C#','C++'] 
y = [22.2, 17.6, 8.8, 8, 7.7, 6.7] 

plt.bar(x, y)
plt.title("Bar Chart")
plt.legend(["bar"])
plt.show()