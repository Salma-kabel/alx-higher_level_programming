#!/usr/bin/python3
"""create a class base class will be the “base” of all other classes"""


class Base():
    """private class attribute"""
    __nb_objects = 0

    """initialization of the class"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
