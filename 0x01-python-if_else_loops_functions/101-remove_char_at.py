#!/usr/bin/python3

def remove_char_at(str, n):
    out = ""
    len1 = len(str)
    i = 0

    while (i != len1):
        if i != n:
            out += str[i]
        i += 1
    return out
