#!/usr/bin/python3
"""function that adds 2 integers if they are int or float"""


def add_integer(a, b=98):
    """adds 2 integers and checks for their type"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
