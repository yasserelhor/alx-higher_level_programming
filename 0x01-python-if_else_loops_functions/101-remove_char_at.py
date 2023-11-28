#!/usr/bin/python3

def remove_char_at(str, n):
    str1 = ""
    for i in str:
        if i != n:
            str1 += i
    return str1
