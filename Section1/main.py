import re
import datetime
from hashlib import sha256
import csv
import os, os.path
from dateutil import parser
import schedule
import re
from datetime import datetime
from hashlib import sha256
import time


NAME = "name"
DOB = "date_of_birth"
EMAIL = "email"
MOBILE_NO = "mobile_no"
format = '%Y/%m/%d'
in_header = {}
fail_header = ["name", "email", "date_of_birth", "mobile_no", "reason"]
success_header = ["first_name", "last_name", "above_18", "membership_ID", "email", "date_of_birth", "mobile_no"]
salutations = ["Mr.", "Ms.", "Mrs.", "DVM", "MD", "DDS", "PhD", "Mdm.", "Dr.", "Miss"]
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')



success = open("success/success.csv", "w", newline='')
fail = open("fail/fail.csv", "w", newline='')
fail_writer = csv.writer(fail, delimiter=',', quoting=csv.QUOTE_MINIMAL)
success_writer = csv.writer(success, delimiter=',', quoting=csv.QUOTE_MINIMAL)
success_writer.writerow(success_header)
fail_writer.writerow(fail_header)

# This function takes in a string parameter 'number' and checks if it is a valid mobile number.
# A valid mobile number is an 8-digit number.
# If the number is valid, the function returns True, otherwise it returns False.

def check_mobile_number(number):
    """
    This function takes in a string parameter 'number' and checks if it is a valid mobile number.
    A valid mobile number is an 8-digit number.
    If the number is valid, the function returns True, otherwise it returns False.
    """

    if re.match(pattern="^\d{8}$", string=str(number)):
        return True
    return False

# This function takes in a parameter 'birthday' in the format '%m/%d/%y' and calculates the age based on the current date.
# If the age is greater than 18, the function returns True, otherwise it returns False.

def check_age(birthday):
    """
    This function takes in a parameter 'birthday' in the format '%Y/%m/%d' and calculates the age based on the 01/01/2022.
    If the age is greater than 18, the function returns True, otherwise it returns False.
    """
    global format
    birthday = clean_time(str(birthday))
    now = clean_time("2022/01/01")  # Now
    duration = datetime.strptime(now, format) - datetime.strptime(birthday,format)
    seconds = duration.total_seconds()
    age = divmod(seconds,31536000)[0]
    return age > 18

# This function takes in a date parameter 'date' in the format '%m/%d/%y' or '%m-%d-%y' and returns a datetime object.

def clean_time(date):
    """
    This function takes in a date parameter 'date' in the format '%m/%d/%y' or '%m-%d-%y' and returns a datetime object.
    """
    date = parser.parse(date)
    global format
    return date.strftime(format)

# This function takes in a string parameter 'email' and checks if it is a valid email address.
# A valid email address must have a domain of either 'com' or 'net'.
# If the email address is valid, the function returns True, otherwise it returns False.

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

# This function takes in a string parameter 'name' and removes any salutations from the name.
# The function then returns the first and last names as separate strings.

def filterSalutations(name):
    """
    This function takes in a string parameter 'name' and removes any salutations from the name.
    The function then returns the first and last names as separate strings.
    """

    for item in salutations:
        if item in name:
            name = name.replace(item, "")
    name = name.strip()
    names = name.split(" ")
    first = names[0]
    last = ""
    for i in range(1, len(names)):
        last = last + names[i]
    return first, last

# This function takes in a date parameter 'birthday' in the format '%m/%d/%y' and returns a string formpython -m pydoc sysatted as '%Y%m%d'.
#

def check_name(name):
    """
     Check if a given name is valid.

     Parameters:
     name (str): The name to be checked.

     Returns:
     bool: True if the name is valid, False otherwise.
     """
    if name is None or name == "":
        return False
    return True

def read_csv(filename):
    """
    Reads a CSV file and returns the data as a list of rows.

    Args:
        filename (str): The name of the CSV file to read.

    Returns:
        list: A list of lists, where each inner list represents a row in the CSV file.

    Raises:
        FileNotFoundError: If the specified CSV file cannot be found.

    """
    global in_header
    filepath = "in\\"+ str(filename)
    infile = open(filepath, newline="")
    csvreader = csv.reader(infile)
    out = []
    i = 0
    for row in csvreader:
        if i > 0:
            out.append(row)
        if i == 0:
            for j in range(len(row)):
                in_header[row[j].strip()] = j
        i = i+1

    return out



def generate_failed_applicant(data, reason):
    """
    Generates a row in the output file for failed applicants, with the provided reason.

    Args:
    data: A list containing the data for a failed applicant.
    reason: A string containing the reason for the applicant's failure.

    Returns:
    None.
    """
    global fail_writer
    out = []
    for item in data:
        out.append(item)
    out.append(reason)

    fail_writer.writerow(out)

def generate_successul_applicants(first, last, above_18, membership_id,email, birthday, mobile_no):
    global success_writer
    """
      Writes a successful applicant's information to a CSV file.

      Args:
          first (str): The applicant's first name.
          last (str): The applicant's last name.
          above_18 (str): A string representation of whether the applicant is over 18 years old ("Yes" or "No").
          membership_id (str): The applicant's membership ID.
          email (str): The applicant's email address.
          birthday (str): The applicant's date of birth in the format MM/DD/YYYY.
          mobile_no (str): The applicant's mobile number.

      Returns:
          None
      """
    success_writer.writerow([first, last, above_18, membership_id,email, birthday, mobile_no])

def generate_csv(data):
    """
    This function generates a successful applicant record if the input data passes certain validation checks.
    If any of the validation checks fail, the function generates a failed applicant record with a reason for failure.
    The input data is expected to be in CSV format, with the headers defined in the global variable 'in_header'.

    Args:
    data (list): A list representing a single row of input data from the CSV file.

    Returns:
    None.

    Raises:
    None.
    """
    if check_mobile_number(data[in_header[("%s" % MOBILE_NO)]]):
        mobile_no = data[in_header[MOBILE_NO]]
    else:
        generate_failed_applicant(data, "MOBILE NUMBER NOT 8 DIGITS")
        return
    if check_email(data[in_header[("%s" % EMAIL)]]):
        email = data[in_header[EMAIL]]
    else:
        generate_failed_applicant(data, "EMAIL NOT .NET OR .COM")
        return
    if check_age(data[in_header[("%s" % DOB)]]):
        birthday = clean_time(str(data[in_header[DOB]]))
        above_18 = "Yes"
    else:
        generate_failed_applicant(data, "BELOW 18")
        return
    if check_name(data[in_header[("%s" % NAME)]]):
        first ,last = filterSalutations(data[in_header[NAME]])
    else:
        generate_failed_applicant(data, "EMPTY NAME")
        return
    birthday = birthday.replace("/", "").strip()
    hash = sha256(birthday.encode('utf-8')).hexdigest()[0:5]
    membership_id = last.strip() + "_" + str(hash).strip()
    generate_successul_applicants(first, last, above_18, membership_id,email, birthday, mobile_no)

def run_job():
    """
    it loops through all
    files in the "in" directory and reads each file as a CSV using the read_csv() function. Then, for each row in the
    CSV, the generate_csv() function is called to generate a membership ID and check if the data is valid. If the data
     is valid, it is written to the successful applicants CSV file using the generate_successul_applicants() function.
    Otherwise, it is written to the failed applicants CSV file using the generate_failed_applicant() function.
      """
    # Loop through all files in the "in" directory
    for filename in os.listdir("in"):
        # Read the CSV file and store the data as a list of rows
        data = read_csv(filename)
        # Loop through each row in the CSV data
        for item in data:
            # Generate a membership ID and check if the data is valid
            generate_csv(item)


if __name__ == '__main__':
    """
    This code block checks if the current script is being run as the main program. If so, runs the job every hour"""
    # If this script is being run as the main program
    schedule.every().hour.do(run_job)
    while True:
        schedule.run_pending()
        time.sleep(1)

