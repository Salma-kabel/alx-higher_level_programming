#!/usr/bin/python3
"""function that writes a string to a file"""


def write_file(filename="", text=""):
    """opens a file"""
    with open(filename, mode='w', encoding="utf-8") as f:
        wr = f.write(text)
        return wr
