#!/usr/bin/python3
"""
Writes text to a file and returns the character count.

Usage: char_count = write_file("filename.txt", "Your text here")
"""


def write_file(filename="", text=""):
    """
    Parameters: filename (str), text (str)
    Returns: int (character count)
    """
    char = 0
    for i in text:
        char += 1

    with open(filename, 'w', encoding='UTF-8',) as F:
        F.write(text)

    return char
