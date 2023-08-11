#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum_ = 0 
    for i in range(len(sys.argv) - 1):
        sum_ = sum_ + int(sys.argv[i + 1])
    print(f"{sum_}")
