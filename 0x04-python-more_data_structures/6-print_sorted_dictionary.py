#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    for item, key in sorted(a_dictionary.items()):
        print("{}: {}".format(item, key))
