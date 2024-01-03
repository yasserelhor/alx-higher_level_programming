#!/usr/bin/python3
"""
Module text_indentation
This module defines a function text_indentation
that adds two new lines after each occurrence
of the characters '.', '?', and ':' in the given text.
"""


def text_indentation(text):
    """
    Prints text with added two newlines
    after each occurrence of the characters '.', '?', and ':'.

    Parameters:
    - text (str): The input text.

    Raises:
    - TypeError: If text is not a string.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")

