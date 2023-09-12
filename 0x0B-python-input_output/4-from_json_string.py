#!/usr/bin/python3
"""Return the Python object representation of a JSON string."""
import json


def from_json_string(my_str):
    """uses json module"""
    return json.loads(my_str)
