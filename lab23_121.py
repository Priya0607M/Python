#Write a code combine PAN CARD NUMBER and EMAIL ID validations into a single program

import re

def validate_pan(pan):
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    if re.match(pattern, pan):
        return True
    return False

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False

pan_number = input("Enter PAN card number: ")
if validate_pan(pan_number):
    print("Valid PAN card number.")
else:
    print("Invalid PAN card number.")
    
email_id = input("Enter email ID: ")
if validate_email(email_id):
    print("Valid email ID.")
else:
    print("Invalid email ID.")
