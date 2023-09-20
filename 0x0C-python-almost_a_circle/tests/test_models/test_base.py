#!/usr/bin/python3
"""test for file base.py"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import pep8


class TestBase(unittest.TestCase):
    """test id attribute"""
    def setUp(self):
        Base._Base__nb_objects = 0
        self.base1 = Base()

    def test_id(self):
        """Test id attribute automatically and with value"""
        self.assertEqual(self.base1.id, 1)
        base2 = Base(89)
        self.assertEqual(base2.id, 89)
        base3 = Base()
        self.assertEqual(base3.id, 2)

    def test_tojsonstring(self):
        self.assertEqual(self.base1.to_json_string(None), "[]")
        self.assertEqual(self.base1.to_json_string([]), "[]")
        res3 = self.base1.to_json_string([{'test1' : 1, 'test2' : None}])
        self.assertEqual(res3, '[{"test1": 1, "test2": null}]')
        self.assertEqual(self.base1.to_json_string([{'test1' : 1}]), '[{"test1": 1}]')

    def test_fromjsonstring(self):
        self.assertEqual(self.base1.from_json_string(None), [])
        self.assertEqual(self.base1.from_json_string("[]"), [])
        res3 = self.base1.from_json_string('[{"test1": 1, "test2": null}]')
        self.assertEqual(res3, [{'test1' : 1, 'test2' : None}])

    def test_pep(self):
        """test for pep8 style"""
        pep = pep8.StyleGuide(quiet=True)
        res = pep.check_files(['models/base.py',
                                        'models/rectangle.py',
                                        'models/square.py'])
        self.assertEqual(res.total_errors, 0,
                         "There is an error")
