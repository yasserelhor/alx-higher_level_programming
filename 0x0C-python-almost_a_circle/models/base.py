#!/usr/bin/python3
"""Module for Base Class"""

class Base:
    """A simple class with a counter for generating unique IDs."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the object with a unique ID.

        Args:
            id (int, optional): The ID to assign to the object. If None, a unique ID
                will be generated using a counter. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects