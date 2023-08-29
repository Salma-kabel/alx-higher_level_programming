#!/usr/bin/python3
"""Create square class"""
class Square:
    """Initialize the class"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """Calculate square area"""
    def area(self):
        return (self.__size * self.__size)
