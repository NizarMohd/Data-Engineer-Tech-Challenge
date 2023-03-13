# Introduction
This Python script is designed to read in a CSV file containing customer data and validate the data before writing the valid data to a new CSV file called "success.csv" and the invalid data to a new CSV file called "fail.csv".

The script uses the following Python modules:

- re: regular expressions library
- datetime: module to work with dates and times
- hashlib: module to work with secure hashes and message digests
- csv: module to work with CSV files
- os: module to work with operating system dependent functionality
- os.path: submodule of os to work with paths in a portable way
- dateutil: library to work with dates and times

## Variables
The script defines the following variables:

- NAME: a string constant representing the "name" header for the CSV file
- DOB: a string constant representing the "date_of_birth" header for the CSV file
- EMAIL: a string constant representing the "email" header for the CSV file
- MOBILE_NO: a string constant representing the "mobile_no" header for the CSV file
- format: a string representing the format of the dates used in the CSV file
- in_header: an empty dictionary which will later be populated with the headers of the input CSV file
- fail_header: a list representing the headers of the output CSV file for invalid data
- success_header: a list representing the headers of the output CSV file for valid data
- salutations: a list representing common salutations to be removed from customer names
- regex: a regular expression pattern used to validate email addresses

The following code imports the required libraries: re, datetime, sha256, csv, os, and dateutil.parser. It also defines some constants such as the header names for input and output files, the date format to be used, and a list of salutations to be removed from names.

The script then opens two csv files, 'success.csv' and 'fail.csv', in write mode, with the 'newline' parameter set to an empty string. It also initializes two csv writer objects with the headers of the two csv files.

The script defines several helper functions that perform different validations and transformations on input data.

- 'check_mobile_number': checks if a given string parameter 'number' is a valid mobile number. A valid mobile number is an 8-digit number. If the number is valid, the function returns True, otherwise it returns False.
- 'check_age': takes in a parameter 'birthday' in the format '%m/%d/%y' and calculates the age based on the current date. If the age is greater than 18, the function returns True, otherwise it returns False.
- 'clean_time': takes in a date parameter 'date' in the format '%m/%d/%y' or '%m-%d-%y' and returns a datetime object in the format '%Y/%m/%d'.
- 'check_email': checks if a given string parameter 'email' is a valid email address. A valid email address must have a domain of either 'com' or 'net'. If the email address is valid, the function returns True, otherwise it returns False.
- 'filterSalutations': takes in a string parameter 'name' and removes any salutations from the name. The function then returns the first and last names as separate strings.
- 'check_name': checks if a given name is valid. If the name is None or empty, the function returns False, otherwise it returns True.
- 'read_csv': reads a CSV file and returns the data as a list of rows.

Overall, the script performs validation and transformation operations on input data and writes the results to the 'success.csv' and 'fail.csv' files
