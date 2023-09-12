#!/usr/bin/python3

""" inserts a line of text to file after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """opens a file"""
    l = ""
    with open(filename) as f:
        for line in f:
            l += line
            if search_string in line:
                l += new_string
    with open(filename, "w") as f:
        f.write(l)
