#!/usr/bin/python3
""" function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """opens a file and append to it"""
    with open(filename, mode='a', encoding="utf-8") as f:
        ad = f.append(text)
        return ad
