#!/usr/bin/python3
"""test for file base.py"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest import TestCase
from unittest.mock import patch


def test_id(unittest.TestCase):
    """ Test id attribute"""
    base1 = base()
    self.assertEqual(base1.id, 1)
    base2 = base(5)
    self.assertEqual(base2.id, 5)
    base3 = base()
    self.assertEqual(base1.id, 3)
