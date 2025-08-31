#1.Write NumPy program to create 3x3 matrix with values ranging from 2 to 10.

import numpy as np
A = np.arange(2,11)
Result = A.reshape(3, 3)
print(Result)

#2.Write a NumPy program to reverse an array (the first element becomes the last)

import numpy as np
l1 = (2,3,4,5)
arr = np.array(l1)
print("Original array : ",arr)
R = arr[::-1]
print("Reversed array : ",R)

#3.Write a NumPy program to find common values between two arrays


import numpy as np
l1 = (2,3,4,5)
ar1 = np.array(l1)
l2 = (2,4,6,8)
ar2 = np.array(l2)
Common_values = np.intersect1d(ar1, ar2)
print(Common_values)

#4.Write a NumPy program to repeat array elements.

import numpy as np
l1 = (2,3,4,5)
arr = np.array(l1)
Result = np.repeat(arr, 3)
print(Result)

#5.Write a NumPy program to find the memory size of a NumPy array.

import numpy as np
l1 = (2,3,4,5)
arr = np.array(l1)
elements = arr.size
element_size = arr.itemsize
memory = elements*element_size
print("Memory size : ",memory)

#6.Write a NumPy program to create an array of ones and zeros.

import numpy as np
array1 = np.ones([2,3])
array2 = np.zeros([2,3])
final = np.concatenate((array1, array2),axis = 0)
print(final)

#7.Write a NumPy program to find the 4th element of a specified array.

import numpy as np
l1 = (9,3,6,7,5)
arr = np.array(l1)
R = arr.flat[3]
print(R)