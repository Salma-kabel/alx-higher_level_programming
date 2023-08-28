#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end='')
            length += 1
    except:
        break
    print()
    return length
