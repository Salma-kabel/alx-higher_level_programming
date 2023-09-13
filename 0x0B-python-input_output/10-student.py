#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """initialisation"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """ retrieves a dictionary representation"""
    def to_json(self, attrs=None):
        if type(attrs) == list:
            dict_ = {}
            for atrr in self.__dict__:
                for attr2 in attrs:
                    if attr == attr2:
                        dict_[attr] = self.__dict__[attr2]
            return dict_

        return self.__dict__
