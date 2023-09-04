#!/usr/bin/python3
"""Create rectangle class"""


class Rectangle:
    """Initialize the class"""
    def __init__(self, width=0, height=0):
        self.width = width
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
        else:
            self.__width = value

    """Set height"""
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    """calculates area"""
    def area(self):
        return (self.width * self.height)

    """calculates perimeter"""
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return ((2 * self.width) + (2 * self.height))

    """ print the rectangle with the character #"""
    def __str__(self):
        rec = ""
        if self.width == 0 or self.height == 0:
            return (rec)
        for i in range(self.height):
            for j in range(self.width):
                rec += "#"
            rec += "\n"
        return (rec)

    def __repr__(self):
        rec = "Rectangle(%s, %s)" % (self.width, self.height)
        return (rec)
