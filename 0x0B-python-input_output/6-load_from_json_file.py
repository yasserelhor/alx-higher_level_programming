#!/usr/bin/python3
"""
Defines a function for loading a Python object from a JSON file.

Usage: obj = load_from_json_file("filename.json")
"""
import json


def load_from_json_file(filename):
    """Load a Python object from a JSON file."""
    with open(filename) as file:
        return json.load(file)
