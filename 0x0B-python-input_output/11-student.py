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
            atdict = {}
            for atr in attrs:
                for atr2 in self.__dict__:
                    if atr == atr2:
                        atdict[atr] = self.__dict__[atr2]
            return atdict

        return self.__dict__

    """ replaces all attributes of the Student instance"""
    def reload_from_json(self, json):
        for key in json:
            if key == "first_name":
                self.first_name = json[key]
            if key == "last_name":
                self.last_name = json[key]
            if key == "age":
                self.age = json[key]
