#!/usr/bin/python3
"""
Defines a function for converting a JSON string to a Python object.
"""
import json


def from_json_string(my_str):
    """
    Converts a JSON string to a Python object.

    Parameters:
    - my_str (str): The JSON string to be converted.

    Returns:
    - obj: The Python object converted from the JSON string.
    """
    return json.loads(my_str)
