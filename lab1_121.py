
#a.Write a program that displays “Welcome to Python” five times.
print("Welcome to Python\n" * 5)

#b.Write a program that displays the following table:
#    a	 a^2	 a^3
#   1	 1	      1
#   2	 4	      8
#   3	 9	      27
#   4	 16	      64
print("a\t a^2\t a^3")
for a in range(1, 5):
    print(f"{a}\t {a**2}\t      {a**3}")
    

print("\n")

#c.Write a program that displays the result of
Result = (9.5 * 4.5 - 2.5 * 3) / (45.5 - 3.5)
print("The result of given expression is : ",Result)
print("\n")
