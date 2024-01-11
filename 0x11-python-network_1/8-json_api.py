#!/usr/bin/python3

"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


import requests
from sys import argv


if __name__ == "__main__":
    data1 = {'q': ""}
    if len(argv) > 1:
        data1['q'] = argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", data=data1)
    try:
        res = r.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError as e:
        print("Not a valid JSON")
