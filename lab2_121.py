
#Write a python code for calculating the Area and Perimeter of a Rectangle
l = int(input("Enter the lenght of rectangle : "))
b = int(input("Enter the bredth of rectangle : "))
area = l * b;
print("Area of rectangle is : ",area)
perimeter = 2 * (l + b)
print("Perimeter of rectangle is : ",perimeter)

#Write a python code for testing if a number is even or odd
n = int(input("Enter a number : "))
if (n % 2 == 0) : print("Even number")
else : print("Odd number")

#Write a python code for calculate the area and volume of the Cube.
s = int(input("Enter the side of cube : "))
area = 6 * s * s
volume = s * s * s
print("Area of cube : ",area)
print("Volume of cube is : ",volume)

#Write a python code to solve the equation z = (x+y)*(x-y)
x = int(input("Enter value for x : "))
y = int(input("Enter value for y : "))
z = (x+y)*(x-y)
print(z)

#Write a python code to solve the equation z = (x+y)*(x+y)-2xy; write a comment on it. 
x = int(input("Enter value for x : "))
y = int(input("Enter value for y : "))
z = (x+y)*(x+y)-2*x*y
print(z)
#here z = x*x + y*y mathematically

#Write a python code for Converting Celsius to Fahrenhit
c = int(input("Enter temperatire is celcius : "))
f = (c * 9/5)+32
print("Temperature is Fahrenhit is : ",f)