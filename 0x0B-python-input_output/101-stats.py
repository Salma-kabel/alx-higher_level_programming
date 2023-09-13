#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
import sys


def metrics():
    """computes metrics"""
    total_size = 0
    codes = {}
    possible_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0
    try:
        for line in sys.stdin:
            if count == 10:
                print("File size: {}".format(total_size))
                for key in sorted(codes):
                    print("{}: {}".format(key, codes[key]))
                count = 1
            else:
                count += 1
            line = line.split()
            total_size += int(line[-1]) 
            try:
                if line[-2] in possible_codes:
                    if line[-2] in codes.keys():
                        codes[line[-2]] += 1
                    else:
                        codes[line[-2]] = 1
            except IndexError:
                pass
        print("File size: {}".format(total_size))
        for key in sorted(codes):
            print("{}: {}".format(key, codes[key]))
    except KeyboardInterrupt:
        print("File size: {}".format(total_size))
        for key in sorted(codes):
            print("{}: {}".format(key, codes[key]))
        raise


if __name__ == "__main__":

    metrics()
