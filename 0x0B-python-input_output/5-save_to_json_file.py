#!/usr/bin/python3
"""
Defines a function for saving a Python object to a JSON file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using JSON representation.

    Parameters:
    - my_obj: The Python object to be saved.
    - filename (str): The name of the file to save the object to.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
