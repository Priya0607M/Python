# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 13:30:30 2025

@author: Priya
"""

#•Write a Python function to compute the Z-transform of an unit step function. verify whether the system is stable or unstable. 

import sympy as sp

def z_transform_unit_step():
    n, z = sp.symbols('n z')
    
    u_n = 1
    
    U = sp.summation(u_n * z**(-n), (n, 0, sp.oo))
    U_simplified = sp.simplify(U)
    
    print("Z-transform of u[n]:")
    print("U(z) =", U_simplified)
    
    print("\nRegion of Convergence (ROC): |z| > 1")
    
    if 1 > 1:
        print("System is STABLE")
    else:
        print("System is UNSTABLE (unit circle not in ROC)")

z_transform_unit_step()

#Implement this for the system H(z)=0.5(z-0.7)(z-0.9)/(z-0.6)(z-0.4)  and verify whether the system is stable or unstable

import numpy as np

# H(z) = 0.5 (z - 0.7)(z - 0.9) / ((z - 0.6)(z - 0.4))

zeros = np.array([0.7, 0.9])
poles = np.array([0.6, 0.4])
gain = 0.5

print("Zeros of H(z):", zeros)
print("Poles of H(z):", poles)

pole_magnitudes = np.abs(poles)
print("\nPole magnitudes:", pole_magnitudes)

is_stable = np.all(pole_magnitudes < 1)

print("\nStability Analysis:")
if is_stable:
    print("→ The system is STABLE.")
else:
    print("→ The system is UNSTABLE.")
