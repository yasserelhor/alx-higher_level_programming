#!/usr/bin/python3
"""
Add all arguments to a Python list and save them to a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line that contains
            a specified string in a file."""
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
