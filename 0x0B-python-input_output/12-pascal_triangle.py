#!/usr/bin/python3
"""return list of lists of integers representing the Pascal’s triangle"""


def pascal_triangle(n):
    """return pascal's triangle of n"""
    pl_list = []
    if n <= 0:
        return pl_list
    for i in range(1, n + 1):
        in_list = []
        for j in range(i):
            if (j == 0 or j == i - 1):
                in_list.append(1)
            else:
                in_list.append(pl_list[i - 2][j - 1] + pl_list[i - 2][j])
        pl_list.append(in_list)
    return pl_list
