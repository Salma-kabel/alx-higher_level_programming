#!/usr/bin/python3
"""test for file base.py"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch
import pep8


class TestBase(unittest.TestCase):
    """test id attribute"""
    def test_id(self):
        """Test id attribute automatically and with value"""
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base(89)
        self.assertEqual(base2.id, 89)
        base3 = Base()
        self.assertEqual(base3.id, 2)


    def test_pep8(self):
        """test that code follows pep8 style guidelines"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py',
                                        'models/rectangle.py',
                                        'models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
