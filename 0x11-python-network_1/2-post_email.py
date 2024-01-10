#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter
"""

from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    value = {}
    value['email'] = argv[2]
    data = parse.urlencode(value)
    data = data.encode('ascii')
    url = argv[1]
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        page = response.read().decode("utf-8")
        print(page)
