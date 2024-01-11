#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and
password) and uses the GitHub API to display your id
"""


import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(argv[1], argv[2])
    r = requests.get("https://api.github.com/use", auth=auth)
    print(r.json().get("id"))
