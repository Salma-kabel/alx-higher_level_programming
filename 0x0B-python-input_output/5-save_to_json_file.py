#!/usr/bin/python3
"""writes an Object to a file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """opens a file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
