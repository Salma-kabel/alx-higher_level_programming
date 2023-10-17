#!/usr/bin/python3
"""class square iherits from class rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """initialization of square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ return [Square] (<id>) <x>/<y> - <size>"""
        str1 = "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
        return str1

    @property
    def size(self):
        """retrieves size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """set value for width and height"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                    self.height = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = (kwargs[key])
                if key == "size":
                    self.width = (kwargs[key])
                    self.height = (kwargs[key])
                if key == "x":
                    self.x = (kwargs[key])
                if key == "y":
                    self.y = (kwargs[key])

    def to_dictionary(self):
        """ returns the dictionary representation of a Square"""
        dict1 = {}
        dict1["id"] = getattr(self, 'id')
        dict1["size"] = getattr(self, 'width')
        dict1["x"] = getattr(self, 'x')
        dict1["y"] = getattr(self, 'y')
        return dict1
