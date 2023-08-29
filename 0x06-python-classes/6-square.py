#!/usr/bin/python3
"""Create square class"""
class Square():
    """Initialize the class"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
    """Retrieve size"""
    @property
    def size(self):
        return self.__size
    """Retrieve position"""
    @property
    def position(self):
        return self.__position
    """Set size"""
    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    """Set position"""
    @position.setter
    def position(self, value):
        if ((type(value) is not tuple) or (len(value) != 2)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) is not int) or (type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    """Calculate square area"""
    def area(self):
        return(self.__size * self.__size)
    """Print the square"""
    def my_print(self):
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
