#!/usr/bin/python3
"""creates an Object from a "JSON file”"""
import json


def load_from_json_file(filename):
    """opens a file"""
    with open(filename, mode='r', encoding="utf-8") as f:
        return json.load(f)
