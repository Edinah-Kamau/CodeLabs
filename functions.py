import re


def remove_special_characters(s):
    return re.sub(r'[^A-Za-z0-9\s]+', '', s)


"""A function to remove any special characters in the list items"""


def all_unique(listObj):
    return len(listObj) == len(set(listObj))


"""A function that returns True if list has no duplicates"""
