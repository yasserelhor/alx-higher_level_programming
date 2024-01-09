#!/usr/bin/python3
"""Rads files"""


def read_file(filename=""):
    """Print the file"""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
