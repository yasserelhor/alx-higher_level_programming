#!/usr/bin/python3
"""
Appends text to a file and returns the character count.

Usage: char_count = append_write("filename.txt", "Your text here")
"""


def append_write(filename="", text=""):
    """
    Parameters: filename (str), text (str)
    Returns: int (character count)
    """

    with open(filename, "a", encoding='UTF-8',) as F:
        F.write(text)
    return len(text)
