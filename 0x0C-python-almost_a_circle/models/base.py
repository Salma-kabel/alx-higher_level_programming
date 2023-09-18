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

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            obj = cls(5, 9, 0, 0)
        if cls.__name__ == "Square":
            obj = cls(5, 0, 0)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances"""
        filename = cls.__name__ + ".json"
        list1 = []
        if os.path.exists(filename) is False:
            return list1
        with open(filename, mode='r', encoding="utf-8") as f:
            list2 = cls.from_json_string(f.read())
            for instance in list2:
                list1.append(cls.create(**instance))
        return list1
