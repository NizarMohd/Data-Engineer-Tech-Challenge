import re
import datetime
from hashlib import sha256
import csv
import os, os.path
from dateutil import parser

# Constants used in the script
NAME = "name"
DOB = "date_of_birth"
EMAIL = "email"
MOBILE_NO = "mobile_no"
format = '%Y/%m/%d'
in_header = {}
fail_header = ["name", "email", "date_of_birth", "mobile_no", "reason"]
success_header = ["first_name", "last_name", "above_18", "membership_ID", "email", "date_of_birth", "mobile_no"]
salutations = ["Mr.", "Ms.", "Mrs.", "DVM", "MD", "DDS", "PhD", "Mdm."]
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

# Create output CSV files
success = open("success/success.csv", "w", newline='')
fail = open("fail/fail.csv", "w", newline='')
fail_writer = csv.writer(fail, delimiter=',', quoting=csv.QUOTE_MINIMAL)
success_writer = csv.writer(success, delimiter=',', quoting=csv.QUOTE_MINIMAL)

# Write headers to output CSV files
success_writer.writerow(success_header)
fail_writer.writerow(fail_header)

def check_mobile_number(number):
    """
    This function takes in a string parameter 'number' and checks if it is a valid mobile number.
    A valid mobile number is an 8-digit number.
    If the number is valid, the function returns True, otherwise it returns False.
    """
    if re.match(pattern="^\d{8}$", string=str(number)):
        return True
    return False

def check_age(birthday):
    """
    This function takes in a parameter 'birthday' in the format '%Y/%m/%d' and calculates the age based on the 01/01/2022.
    If the age is greater than 18, the function returns True, otherwise it returns False.
    """
    global format
    birthday = clean_time(str(birthday))
    now = clean_time("2022/01/01")
    duration = datetime.strptime(now, format) - datetime.strptime(birthday,format)
    seconds = duration.total_seconds()
    age = divmod(seconds,31536000)[0]
    return age > 18

def clean_time(date):
    """
    This function takes in a date parameter 'date' in the format '%m/%d/%y' or '%m-%d-%y' and returns a datetime object.
    """
    date = parser.parse(date)
    global format
    return date.strftime(format)

def check_email(email):
    """
    This function takes in a string parameter 'email' and checks if it is a valid email address.
    A valid email address must have a domain of either 'com' or 'net'.
    If the email address is valid, the function returns True, otherwise it returns False.
    """
    global regex
    if re.fullmatch(regex, email):
        if email[-3:] == "net" or email[-3:] == "com":
            return True
    return False

def filterSalutations(name):
    """
    This function takes in a string parameter 'name' and removes any salutations from the name.
    The function then returns the first and last names as separate strings.
    """
    for item in salutations:
        if item in name:
            name = name.replace(item, "")
    names = name.split(" ")
    first = names[0]
    last = ""
    for i in range(1, len(names)):
        last = last + names[i]
    return first, last


