
#1.a.	Write a Python program to convert degree to radian
from math import pi
degree = int(input("Enter a value : "))
radian = degree * pi / 180
print(radian)

#2.Make a simplest possible Python program that calculates and prints the
# value of the formula y=6x^2+4sin(x)
from math import sin
x = int(input("Enter a value : "))
y = 6*x*x+4*sin(x)
print(int(y))

#3.	Write a Python function that evaluates the mathematical functions
#f(x)=cos(2x),f^' (x)=-2 sin⁡(2x),and f^'' (x)=-4 cos⁡(2x). 
#	Return these three values. Write out the results of these values for x=π

import math

def trig_function(x):
    f_x = math.cos(2 * x)
    f__x = -2 * math.sin(2 * x)
    f___x = -4 * math.cos(2 * x)
    return f_x, f__x, f___x

from math import pi

x = pi
f_x, f__x, f___x = trig_function(x)
print(f_x)
print(f__x)
print(f___x)
