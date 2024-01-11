#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and
displays the body of the response
"""


from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            print(html)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
