#!/usr/bin/python3
"""Defines a Python function to convert a class instance to
a JSON-compatible dictionary."""


def class_to_json(obj):
    """Converts a class instance to a JSON-compatible dictionary.

    Args:
        obj (object): The class instance to convert.

    Returns:
        dict: A dictionary representing the class instance.
    """
    return obj.__dict__
