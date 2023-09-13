#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """instantiation of class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    """area of rectangle"""
    def area(self):
        return self.__width * self.__height

    """return rectangle description"""
    def __str__(self):
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
