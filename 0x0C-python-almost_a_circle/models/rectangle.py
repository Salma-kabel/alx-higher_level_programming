#!/usr/bin/python3
"""create a rectangle class that inherits from base class"""
from models.base import Base


class Rectangle(Base):
    """Initialization of rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """retrieve width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """validate width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieve height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """validate height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """retrieve x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """validate x attribute"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """retrieve y property"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """return rectangle area"""
        return self.width * self.height

    def display(self):
        """prints the Rectangle instance with the character #"""
        for k in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        string = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

        return string

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.height = args[2]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = (kwargs[key])
                if key == "width":
                    self.width = (kwargs[key])
                if key == "height":
                    self.height = (kwargs[key])
                if key == "x":
                    self.x = (kwargs[key])
                if key == "y":
                    self.y = (kwargs[key])

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dict1 = {}
        dict1["id"] = getattr(self, 'id')
        dict1["width"] = getattr(self, 'width')
        dict1["height"] = getattr(self, 'height')
        dict1["x"] = getattr(self, 'x')
        dict1["y"] = getattr(self, 'y')
        return dict1
