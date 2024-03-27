#!/usr/bin/python3
"""this function finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """functrion"""
    if list_of_integers:
        f = 0
        w = len(list_of_integers) - 1
        while f < w:
            mid = (f+w)//2
            if list_of_integers[mid] > list_of_integers[mid + 1]:
                w = mid
            else:
                f = mid+1
        return list_of_integers[f]
