#!/usr/bin/python3

"""
finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    finds a peak in a list of unsorted ints
    """
    if list_of_integers is None or list_of_integers == []:
        return None
    if len(list_of_integers) == 1:
        return (list_of_integers[0])
    mid = int(len(list_of_integers) / 2)
    if list_of_integers[mid] > list_of_integers[mid - 1] and \
            list_of_integers[mid] > list_of_integers[mid + 1]:
        return list_of_integers[mid]
    num = find_peak(list_of_integers[mid:])
    if num is not None:
        return num
    else:
        return find_peak(list_of_integers[:mid])
                
