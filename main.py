import pandas as pd

"""import pandas"""
import re

""" import re for removing special characters"""

readfile = pd.read_excel('Test Files.xlsx')
"""Read the contents of the xlsx file"""

mylist = readfile['Student Name'].tolist()
"""Covert 'Student Name' contents into a List structure"""


def remove_special_characters(s):
    return re.sub(r'[^A-Za-z0-9\s]+', '', s)


cleaned_mylist = [remove_special_characters(name) for name in mylist]
"""Remove any special characters in the list items"""

# print(readfile)
"""Print the original content of the file"""

# print(mylist)
"""Print the content of the List structure"""

for names in cleaned_mylist:
    emailnames = [names[0].lower() + names.split()[-1].lower() + '@gmail.com']
    print(emailnames)
"""Create email addresses"""


def all_unique(listObj):
    return len(listObj) == len(set(listObj))


"""A function that returns True if list has no duplicates"""

if not all_unique(emailnames):
    print("All elements in list are not unique")
else:
    print("All elements in list are unique")

""" If Statements to check if the email are unique"""

