#!/usr/bin/python3
def no_c(my_string):
    stra = ""
    for c in my_string:
        if c != 'c' and c != 'C':
            stra += c
    return stra
