#!/usr/bin/python3
"""adds all arguments to a list and save them to a file"""
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


try:
    arguments = load_from_json_file("add_item.json")
except FileNotFoundError:
    arguments = list(sys.argv)
save_to_json_file(arguments, "add_item.json")

