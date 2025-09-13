# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 12:02:36 2025

@author: Priya
"""

#a.	Write a program that reads a text file example.txt and counts the number of lines, words, and characters in the file. Print these counts


def analyze_text_file(filename="example.txt"):
    
    line_count = 0
    word_count = 0
    char_count = 0
    with open(r"C:\Users\Priya\Downloads\example.txt",'r') as file:
        for line in file:
            line_count += 1
            char_count += len(line)
            words = line.split()
            word_count += len(words)
            
        print("Number of lines: ",line_count)
        print("Number of words: ",word_count)
        print("Number of characters: ",char_count)

analyze_text_file()

#b.Write a Python program to read a text file line by line and store each line in a list. Print the list after reading the entire file.


lines = []

with open(r"C:\Users\Priya\Downloads\example.txt", 'r') as file:
    for line in file:
        lines.append(line.strip())

print(lines)

#c.Write a Python program to read data from a CSV file data.csv and print each row to the console.

import csv

with open(r"C:\Users\Priya\Downloads\data-1.csv",'r') as csvfile:
   
    csv_reader = csv.reader(csvfile)

    for row in csv_reader:
        print(row)
        
#d.Write a Python program that merges the contents of two text files file1.txt and file2.txt into a third file merged.txt. Ensure that the contents of file1.txt come first.        

with open("file1.txt", "w") as f:
    f.write("ICT DEPARTMENT")

with open("file2.txt", "w") as f:
    f.write(" 3EK2")

with open("file1.txt", "r") as f1:
    content1 = f1.read()

with open("file2.txt", "r") as f2:
    content2 = f2.read()

with open("merged.txt", "w") as merged_file:
    merged_file.write(content1)
    merged_file.write(content2)

print("Files merged successfully into merged.txt")

with open("merged.txt", "r") as merged_file:
    print("Content of merged.txt:")
    print(merged_file.read())


