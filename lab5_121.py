
#a. Write a Python program to Count the occurrences of an element in a tuple.
t1 = (1,2,3,2,4,3,5,3,5,6,5,7,1,2)
print(t1.count(3))

#b.	Write a Python program to Check if an element exists in a tuple.
t2 = (2,4,1,5,3,6,8,7,9,4,5,4,1,4)
print("1 found at index : ",t2.index(1))

#c.	Write a Python program to Convert a tuple to a string.
t3 = (1,2,3,4)
result = str(t3)
print(result)

#d.	Write a Python program to Find the maximum and minimum elements in a tuple.
t4 = (1,2,3,4)

max = t4[0]
min = t4[0]

for x in t4[0:]:
    if x > max:
        max = x
    if x < min:
        min = x

print("Max:", max)
print("Min:", min)

#e.	Write a Python program to convert a tuple of strings to a single string.
t5 = ("Python ", "is ", "OOP concept")
string = ""
for i in t5:
    string = string + i
print(string)

#f.	Write a Python program to sort a tuple of integers.

print(tuple(range(0,8)))
print(tuple(range(7,-1,-1)))

#g.	Write a python program to find the first and last elements of a tuple

t7 = (1,2,3,4,5)
print("First element : ",t7[0])
print("Last element : ",t7[-1])
