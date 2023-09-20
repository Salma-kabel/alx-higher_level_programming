import unittest
from models.square import Square
import pep8
from models.rectangle import Rectangle
from models.base import Base

"""test for square class"""


class test_square(unittest.TestCase):
    """run before any test"""
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_init_square(self):
        """test for inistantiation function"""
        sq0 = Square(5)
        self.assertEqual(sq0.width, 5)
        self.assertEqual(sq0.height, 5)
        self.assertEqual(sq0.size, 5)
        self.assertEqual(sq0.x, 0)
        self.assertEqual(sq0.y, 0)
        self.assertEqual(sq0.id, 1)
        sq1 = Square(4, 3)
        self.assertEqual(sq1.size, 4)
        self.assertEqual(sq1.width, 4)
        self.assertEqual(sq1.height, 4)
        self.assertEqual(sq1.x, 3)
        self.assertEqual(sq1.y, 0)
        self.assertEqual(sq1.id, 2)
        sq2 = Square(10, 2, 1, 50)
        self.assertEqual(sq2.width, 10)
        self.assertEqual(sq2.height, 10)
        self.assertEqual(sq2.size, 10)
        self.assertEqual(sq2.x, 2)
        self.assertEqual(sq2.y, 1)
        self.assertEqual(sq2.id, 50)
        sq3 = Square(20, 1)
        self.assertEqual(sq3.width, 20)
        self.assertEqual(sq3.height, 20)
        self.assertEqual(sq3.size, 20)
        self.assertEqual(sq3.x, 1)
        self.assertEqual(sq3.y, 0)
        self.assertEqual(sq3.id, 3)
        self.assertRaises(TypeError, sq1.__init__, "1", 8, 1)
        self.assertRaises(TypeError, sq1.__init__, 20, "5", 1)
        self.assertRaises(TypeError, sq1.__init__, 20, 8, "1")
        self.assertRaises(ValueError, sq1.__init__, 0, 8, 1)
        self.assertRaises(ValueError, sq1.__init__, -20, 8, 1)
        self.assertRaises(ValueError, sq1.__init__, 20, -8, 1)
        self.assertRaises(ValueError, sq1.__init__, 20, 8, -1)
