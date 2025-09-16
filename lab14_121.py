# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 11:38:14 2025

@author: Priya
"""

#a)Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())

#b) Create a class Book that stores details like the title, author, and price of a book. Add methods to display the details of the book and apply a discount to the price. 
#---> Create two objects for different books and display their details. 
#---> Apply a 10% discount to one of the books and display the updated price

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price  

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price:.2f}") 

    def discount(self, percent):
        discount = self.price * (percent / 100)
        self.price = self.price - discount

book1 = Book("The Murder Book", "Mark Billingham", 449.00)
book2 = Book("It starts with us", "Collen Hoover", 190.00)

print("Book 1 :")
book1.display_details()

print("Book 2 :")
book2.display_details()

print("Applying 10% discount to Book 1\n")
book1.discount(10)
print("Book 1 updated :")
book1.display_details()
