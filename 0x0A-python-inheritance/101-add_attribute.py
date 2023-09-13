#!/usr/bin/python3
"""adds a new attribute to an object if it’s possible"""


def add_attribute(obj, name, value):
    """adds a new attribute"""
    if hasattr(obj, "__dict__") is True:
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
