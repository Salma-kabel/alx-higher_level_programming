#!/usr/bin/python3
"""return list of available attributes and methods"""


def lookup(obj):
    """attributes and methods of an object"""
    return obj.__dict__
