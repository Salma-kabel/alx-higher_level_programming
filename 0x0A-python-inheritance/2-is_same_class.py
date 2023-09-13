#!/usr/bin/python3
"""checks if the object is exactly an instance of the class"""


def is_same_class(obj, a_class):
    """ returns True if the object is an instance of the class"""
    if type(obj) is a_class:
        return True
    else:
        return False
