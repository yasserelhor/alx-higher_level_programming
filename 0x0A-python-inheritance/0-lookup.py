#!/usr/bin/python3
"""Defines a function for retrieving a list of an object's attributes."""


def lookup(obj):
    """Return a list of available attributes for the given object."""
    return dir(obj)
