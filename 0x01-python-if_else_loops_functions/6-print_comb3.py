#!/usr/bin/python3
for i in range(0, 100):
    if i == 89:
        print("{}".format(i))
    else:
        if (i % 10) > (i / 10):
            print("{:02d}".format(i), end=", ")
