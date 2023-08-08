#!/usr/bin/python3
num = 0
for character in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(character - num)), end="")
    num = 32 if num == 0 else 0
