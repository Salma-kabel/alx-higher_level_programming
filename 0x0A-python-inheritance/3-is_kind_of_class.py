#!/usr/bin/python3
"""checks if the object is an instance of, or if the object is
instance of a class that inherited from, the specified class"""


def is_kind_of_class(obj, a_class):
    """return true if the object is an instance of, or if the object is
instance of a class that inherited from, the specified class"""

    return (isinstance(obj, a_class))
