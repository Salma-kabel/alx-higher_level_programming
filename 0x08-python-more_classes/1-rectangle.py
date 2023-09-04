#!/usr/bin/python3
"""Create rectangle class"""


class Rectangle:
    """Initialize the class"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.height = height

    """Retrieve width"""
    @property
    def width(self):
        return (self.__width)

    """Retrieve height"""
    @property
    def height(self):
        return (self.__height)

    """Set width"""
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    """Set height"""
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
