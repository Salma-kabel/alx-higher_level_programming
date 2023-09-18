#!/usr/bin/python3
"""create a class base class will be the “base” of all other classes"""
import json


class Base():
    """private class attribute"""
    __nb_objects = 0

    """initialization of the class"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        list1 = []
        if list_objs is None:
            pass
        else:
            for i in range(len(list_objs)):
                list1.append(list_objs[i].to_dictionary())
        list2 = cls.to_json_string(list1)

        with open(filename, mode='w', encoding="utf-8") as f:
            f.write(list2)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        list1 = []
        if json_string is None:
            return list1
        return json.loads(json_string)
