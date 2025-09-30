# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 14:47:55 2025

@author: Priya
"""

#Using Python, compute the Z-transform of the sequence x[n]=3^n u[n].
import sympy as sp
n, z, a = sp.symbols('n z a')

x_n = 3**n
X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))

print("Z-transform of x[n] = 3^n u[n]:")
sp.pprint(X_z, use_unicode=True)

#Using Python, compute the Z-transform of the sequence x[n]=cos⁡(wn)u[n]. 
import sympy as sp

n, z, omega = sp.symbols('n z omega')

x_n = sp.cos(omega * n)
X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))

print("Z-transform of x[n] = cos(omega * n) u[n]:")
sp.pprint(X_z, use_unicode=True)

