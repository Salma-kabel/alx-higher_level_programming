#!/usr/bin/python3

""" inserts a line to file after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """opens a file"""
    line_ = ""
    with open(filename) as f:
        for line in f:
            line_ += line
            if search_string in line:
                line_ += new_string
    with open(filename, "w") as f:
        f.write(line_)
