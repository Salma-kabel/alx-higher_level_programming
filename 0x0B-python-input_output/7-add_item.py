#!/usr/bin/python3
"""adds all arguments to a list and save them to a file"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    arguments = load_from_json_file("add_item.json")
except FileNotFoundError:
    arguments = []
arguments.extend(sys.argv[1:])
save_to_json_file(arguments, "add_item.json")

