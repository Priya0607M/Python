#a.Write a Python program to print all odd numbers between 1 to 100 using a while loop.
i=1
while i<=100:
    print(i,end=" ")
    i+=2

#b.Write a Python program to find the sum of all natural numbers between 1 to n.
n = int(input("Enter the number of terms : "))   
sum=0
for i in range (1,n):
    sum = sum + i

print(sum)

#c.	Write a Python function program to count a number of digits in a number.
n = int(input("Enter a number"))
digits = 0
while(n>0):
     n = n//10
     digits+=1
     
print(digits)

#d.	Write a Python program to find the first and last digits of a number.    
n = int(input("Enter a number: "))
l = n%10
while n>0:
    r = n%10
    n = n//10
    
print("first_digit:",r)
print("last_digit: ",l)    

#e.	Write a Python program to swap the first and last digits of a number.
n = int(input("Enter a number: "))
l = n%10
while n>0:
    r = n%10
    n = n//10
    
print("first_digit:",r)
print("last_digit: ",l)

#f.	Write a Python program to calculate the product of digits of a number.
n = int(input("Enter a number: "))
pro = 1
while n>0:
    r = n%10
    n = n//10
    pro = pro*r
    
print("Product of terms : ",pro)

#g.	Write a Python program to enter a number and print its reverse
n = int(input("Enter a number: "))
Rev = 0
while n>0:
    r = n%10
    n = n//10
    Rev = Rev*10+r
    
print("Reverse of number : ",Rev)

