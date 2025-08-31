
#a.	Write a Python program to multiply all the items in a list.
import math
list = [2,3,4]
print("Product of all terms of the list : ",math.prod(list))
    
#b.	Write a Python program to get the largest number from a list.
list = [21.23,21.12,21.00]
print("The largest number from the given list : ",max(list))

#c.	Write a Python program to remove duplicates from a list.

list_1 = [1,1,2,3,4,4,5]
list_ = list(dict.fromkeys(list_1))
print("List after removing the duplicates : ",list_)

#d.	Write a Python program to get the frequency of elements in a list.
from collections import Counter

list = [5, 1, 2, 2, 4, 3, 1, 2, 3, 1, 1, 5, 2]
frequency = Counter(list)
print(frequency)  
 
#e.	Find common items from two lists
list1 = [1, 2, 3, 4, 5, 2]
list2 = [4, 5, 6, 7, 8, 4]

set1 = set(list1)
set2 = set(list2)

common_set = set1 & set2

common_list = list(common_set)

print("Common elements: ",common_list)

#f.	Convert a list of multiple integers into a single integer
list = [1, 2, 3, 4]
result = int(''.join(map(str, list)))
print(result)
