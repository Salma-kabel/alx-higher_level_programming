#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """initialisation"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """ retrieves a dictionary representation"""
    def to_json(self):
        return self.__dict__
