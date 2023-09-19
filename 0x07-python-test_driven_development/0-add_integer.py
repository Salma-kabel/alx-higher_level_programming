#!/usr/bin/python3
"""function that adds 2 integers."""


def add_integer(a, b=98):
    """adds 2 integers."""
    if type(a) is not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) is not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
