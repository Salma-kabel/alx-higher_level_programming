import unittest
import os
from models.square import Square
import pep8
from models.rectangle import Rectangle
from models.base import Base

"""test for square class"""


class test_square(unittest.TestCase):
    """run before any test"""
    def setUp(self):
        Base._Base__nb_objects = 0
        self.sq= Square(5, 2, 1, 13)
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


    def test_str_square(self):
        """test str method for square"""
        self.assertEqual(self.sq.__str__(), "[Square] (13) 2/1 - 5")

    def test_todict_square(self):
        """test to_dictionary method for square"""
        res = {'id' : 13, 'size': 5, 'x' : 2, 'y' : 1}
        self.assertEqual(self.sq.to_dictionary(),res)

    def test_update_square(self):
        """test for update method for square"""
        self.assertEqual(self.sq.update(None), None)
        self.assertEqual(self.sq.update(), None)
        self.sq.update(7)
        self.assertEqual(self.sq.id, 7)
        self.sq.update(9, 12)
        self.assertEqual(self.sq.id, 9)
        self.assertEqual(self.sq.width, 12)
        self.assertEqual(self.sq.height, 12)
        self.sq.update(41, 13, 5)
        self.assertEqual(self.sq.id, 41)
        self.assertEqual(self.sq.width, 13)
        self.assertEqual(self.sq.height, 13)
        self.assertEqual(self.sq.x, 5)
        self.sq.update(42, 15, 7, 2)
        self.assertEqual(self.sq.id, 42)
        self.assertEqual(self.sq.width, 15)
        self.assertEqual(self.sq.height, 15)
        self.assertEqual(self.sq.x, 7)
        self.assertEqual(self.sq.y, 2)
        self.sq.update(**{'id' : 8})
        self.assertEqual(self.sq.id, 8)
        self.sq.update(**{'id' : 8, 'size': 7})
        self.assertEqual(self.sq.width, 7)
        self.assertEqual(self.sq.height, 7)
        self.sq.update(**{'id' : 8, 'size': 7, 'x' : 2})
        self.assertEqual(self.sq.x, 2)
        self.sq.update(**{'id' : 8, 'size': 7, 'x' : 2, 'y': 1})
        self.assertEqual(self.sq.y, 1)

    def test_create_square(self):
        """test for create for square"""
        sq1 = Square.create(**{'id' : 5})
        self.assertEqual(sq1.id, 5)
        sq2 = Square.create(**{'id' : 6, 'size' : 7})
        self.assertEqual(sq2.id, 6)
        self.assertEqual(sq2.width, 7)
        self.assertEqual(sq2.height, 7)
        sq4 = Square.create(**{'id' : 11, 'size' : 7, 'x': 3})
        self.assertEqual(sq4.id, 11)
        self.assertEqual(sq4.width, 7)
        self.assertEqual(sq4.height, 7)
        self.assertEqual(sq4.x, 3)
        sq5 = Square.create(**{'id' : 15, 'size' : 7, 'x': 1, 'y' : 1})
        self.assertEqual(sq5.id, 15)
        self.assertEqual(sq5.width, 7)
        self.assertEqual(sq5.height, 7)
        self.assertEqual(sq5.x, 1)
        self.assertEqual(sq5.y, 1)

    def test_saveto_square(self):
        """test save_to_file for square"""
        Square.save_to_file(None)
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")
        list1 = [Square(4), Square(7, 2, 1)]
        Square.save_to_file(list1)
        list2 = []
        for i in range(2):
                list2.append(list1[i].to_dictionary())
        with open("Square.json") as f:
            self.assertEqual(f.read(), Square.to_json_string(list2))

    def test_loadfrom_square(self):
        """test load_from_file for Square"""
        os.remove("Square.json")
        list2 = []
        self.assertEqual(Square.load_from_file(), list2)
        list1 = [Square(4), Square(3, 2, 1)]
        Square.save_to_file(list1)
        list0 = Square.load_from_file()
        list2 = []
        list3 = []
        for i in range(2):
            list2.append(list1[i].to_dictionary())
        for instance in list2:
                list3.append(Square.create(**instance))
        for i in range(len(list3)):
            self.assertEqual(list3[i].__str__(), list0[i].__str__())

