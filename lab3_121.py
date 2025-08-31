
#a.	Write a Python program to reverse a string.

def reverse_string(s):
    return s[::-1]

str = input("Enter a string: ")
reversed_str = reverse_string(str)
print("Reversed string:", reversed_str)

#b.	Write a Python program to check if a string is a palindrome.

def is_palindrome(s):
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

str = input("Enter text: ")
if is_palindrome(str):
    print("It’s a palindrome.")
else:
    print("Not a palindrome.")
    
#c.	Write a Python program to check if a string contains only digits.

def only_digits(s):
    return s.isdigit()

str = input("Enter a string: ")

if only_digits(str):
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")
    
#d.	Write a Python program to find the longest word in a sentence

def longest_word(sentence):
    words = sentence.split()         
    return max(words, key=len)      

sentence = input("Enter a sentence: ")
print("Longest word is:", longest_word(sentence))
   
#e.	Write a Python program to find the length of the last word in a sentence.

def lengthof_lastword(s):
    words = s.split()
    return len(words[-1]) if words else 0

print(lengthof_lastword("ICT DEPARTMENT"))