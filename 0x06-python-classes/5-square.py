#!/usr/bin/python3
"""Create square class"""
class Square():
    """Initialize the class"""
    def __init__(self, size=0):
        self.__size = size
    """Retrieve size"""
    @property
    def size(self):
        return self.__size
    """Set size and value"""
    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
    """Calculate square area"""
    def area(self):
        return(self.__size * self.__size)
    """Print the square"""
    def my_print(self):
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
