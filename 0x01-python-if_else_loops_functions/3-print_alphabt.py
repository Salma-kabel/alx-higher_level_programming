#!/usr/bin/python3
for i in range(0, 26):
    if chr(i + 97) != 'q' and chr(i + 97) != 'e':
        print("{}".format(chr(i + 97)), end = "")
