#!/usr/bin/python3
"""function to read text file and prints to stdout"""


def read_file(filename=""):
    with open(filename, mode='r', encoding="utf-8") as f:
        print(f.read(), end="")
