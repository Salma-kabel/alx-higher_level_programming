#!/usr/bin/python3
"""class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """instantiation of class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    """area of square"""
    def area(self):
        return self.__size * self.__size
