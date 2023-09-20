import unittest
import pep8
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import io
import sys

"""test for rectangle class"""


class TestRectangle(unittest.TestCase):
    """test for every method"""
    def setUp(self):
        """create an instance before any test"""
        Base._Base__nb_objects = 0
        self.rect = Rectangle(3, 2, 2, 1, 10)

    def test_init(self):
        """test for inistantiation function"""
        rect1 = Rectangle(4, 3)
        self.assertEqual(rect1.width, 4)
        self.assertEqual(rect1.height, 3)
        self.assertEqual(rect1.x, 0)
        self.assertEqual(rect1.y, 0)
        self.assertEqual(rect1.id, 1)
        rect2 = Rectangle(10, 4, 2, 1, 50)
        self.assertEqual(rect2.width, 10)
        self.assertEqual(rect2.height, 4)
        self.assertEqual(rect2.x, 2)
        self.assertEqual(rect2.y, 1)
        self.assertEqual(rect2.id, 50)
        rect3 = Rectangle(20, 8, 1)
        self.assertEqual(rect3.width, 20)
        self.assertEqual(rect3.height, 8)
        self.assertEqual(rect3.x, 1)
        self.assertEqual(rect3.y, 0)
        self.assertEqual(rect3.id, 2)
        self.assertRaises(TypeError, rect1.__init__, "1", 8, 1)
        self.assertRaises(TypeError, rect1.__init__, 20, "5", 1)
        self.assertRaises(TypeError, rect1.__init__, 20, 8, "1")
        self.assertRaises(TypeError, rect1.__init__, 20, 8, 1, "3")
        self.assertRaises(ValueError, rect1.__init__, 0, 8, 1)
        self.assertRaises(ValueError, rect1.__init__, 10, 0, 1)
        self.assertRaises(ValueError, rect1.__init__, -20, 8, 1)
        self.assertRaises(ValueError, rect1.__init__, 20, -8, 1)
        self.assertRaises(ValueError, rect1.__init__, 20, 8, -1)
        self.assertRaises(ValueError, rect1.__init__, 20, 8, 1, -1)

    def test_area(self):
        """test area method"""
        self.assertEqual(self.rect.area(), 6)

    def test_str(self):
        """test str method"""
        self.assertEqual(self.rect.__str__(), "[Rectangle] (10) 2/1 - 3/2")

    def test_display(self):
        """test for display method"""
        sys.stdout = io.StringIO()
        self.rect.display()
        self.assertEqual(sys.stdout.getvalue(), "\n  ###\n  ###\n")
        self.rect.x = 0
        sys.stdout = io.StringIO()
        self.rect.display()
        self.assertEqual(sys.stdout.getvalue(), "\n###\n###\n")
        self.rect.x = 2
        self.rect.y = 0
        sys.stdout = io.StringIO()
        self.rect.display()
        self.assertEqual(sys.stdout.getvalue(), "  ###\n  ###\n")
        self.rect.x = 0
        sys.stdout = io.StringIO()
        self.rect.display()
        self.assertEqual(sys.stdout.getvalue(), "###\n###\n")

    def test_todict(self):
        """test to_dictionary method"""
        res = {'id' : 10, 'width' : 3, 'height' : 2, 'x' : 2, 'y' : 1}
        self.assertEqual(self.rect.to_dictionary(),res)

    def test_update(self):
        """test for update method"""
        self.assertEqual(self.rect.update(None), None)
        self.assertEqual(self.rect.update(), None)
        self.rect.update(7)
        self.assertEqual(self.rect.id, 7)
        self.rect.update(9, 12)
        self.assertEqual(self.rect.id, 9)
        self.assertEqual(self.rect.width, 12)
        self.rect.update(41, 13, 5)
        self.assertEqual(self.rect.id, 41)
        self.assertEqual(self.rect.width, 13)
        self.assertEqual(self.rect.height, 5)
        self.rect.update(42, 15, 7, 2)
        self.assertEqual(self.rect.id, 42)
        self.assertEqual(self.rect.width, 15)
        self.assertEqual(self.rect.height, 7)
        self.assertEqual(self.rect.x, 2)
        self.rect.update(45, 15, 9, 4, 2)
        self.assertEqual(self.rect.id, 45)
        self.assertEqual(self.rect.width, 15)
        self.assertEqual(self.rect.height, 9)
        self.assertEqual(self.rect.x, 4)
        self.assertEqual(self.rect.y, 2)
        self.rect.update(**{'id' : 8})
        self.assertEqual(self.rect.id, 8)
        self.rect.update(**{'id' : 8, 'width': 7})
        self.assertEqual(self.rect.width, 7)
        self.rect.update(**{'id' : 8, 'width': 7, 'height' : 3})
        self.assertEqual(self.rect.height, 3)
        self.rect.update(**{'id' : 8, 'width': 7, 'height' : 3, 'x' : 2})
        self.assertEqual(self.rect.x, 2)
        self.rect.update(**{'id' : 8, 'width': 7, 'height' : 3, 'x' : 2, 'y': 1})
        self.assertEqual(self.rect.y, 1)


    def test_create_rect(self):
        rect1 = Rectangle.create(**{'id' : 5})
        self.assertEqual(rect1.id, 5)
        rect2 = Rectangle.create(**{'id' : 6, 'width' : 7})
        self.assertEqual(rect2.id, 6)
        self.assertEqual(rect2.width, 7)
        rect3 = Rectangle.create(**{'id' : 10, 'width' : 7, 'height' : 5})
        self.assertEqual(rect3.id, 10)
        self.assertEqual(rect3.width, 7)
        self.assertEqual(rect3.height, 5)
        rect4 = Rectangle.create(**{'id' : 11, 'width' : 7, 'height' : 5, 'x': 3})
        self.assertEqual(rect4.id, 11)
        self.assertEqual(rect4.width, 7)
        self.assertEqual(rect4.height, 5)
        self.assertEqual(rect4.x, 3)
        rect5 = Rectangle.create(**{'id' : 15, 'width' : 7, 'height' : 4, 'x': 1, 'y' : 1})
        self.assertEqual(rect5.id, 15)
        self.assertEqual(rect5.width, 7)
        self.assertEqual(rect5.height, 4)
        self.assertEqual(rect5.x, 1)
        self.assertEqual(rect5.y, 1)
def test_pep8(self):
        """test that code follows pep8 style guidelines"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py',
                                        'models/rectangle.py',
                                        'models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
