#!/usr/bin/python3
"""function to read text file and prints to stdout"""


def read_file(filename=""):
    """opening a file"""
    with open(filename, mode='r', encoding="utf-8") as f:
        rd = f.read()
        print("{}".format(rd))
