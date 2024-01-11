#!/usr/bin/python3
"""
script that takes 2 arguments
in order to solve this challenge
"""


import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])
    r = requests.get(url)
    list1 = r.json()
    i = 0
    for commit in list1:
        if i == 10:
            break
        print("{}: {}".format(
            commit.get('sha'),
            commit.get('commit').get('author').get('name')))
        i = i + 1
