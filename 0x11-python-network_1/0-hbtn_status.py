#!/bin/bash/python3
#script that fetches https://alx-intranet.hbtn.io/status

import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode(encoding='utf-8')))
