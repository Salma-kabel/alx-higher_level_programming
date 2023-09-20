import unittest
import pep8
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
"""test for rectangle class"""


class TestRectangle(unittest.Testcase):
    """test for every method"""
    def setUp(self):
        """create an instance before any test"""

    def test_init(self):
        """test for inistantiation function"""
        rect1 = Rectangle(4, 3)
        self.assertEqual(rect1.width, 4)
        self.assertEqual(rect1.height, 3)
        self.assertEqual(rect1.x, 0)
        self.assertEqual(rect1,y, 0)
        self.assertEqual(rect1.id, 1)
        rect2 = Rectangle(10, 4, 2, 1, 50)
        self.assertEqual(rect2.width, 10)
        self.assertEqual(rect2.height, 4)
        self.assertEqual(rect2.x, 2)
        self.assertEqual(rect2,y, 1)
        self.assertEqual(rect2.id, 50)
        rect3 = Rectangle(20, 8, 1)
        self.assertEqual(rect3.width, 20)
        self.assertEqual(rect3.height, 8)
        self.assertEqual(rect3.x, 1)
        self.assertEqual(rect3,y, 0)
        self.assertEqual(rect3.id, 2)
