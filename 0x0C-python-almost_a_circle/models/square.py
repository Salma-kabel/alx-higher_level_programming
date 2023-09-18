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
