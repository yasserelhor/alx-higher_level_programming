#!/usr/bin/python3
"""Square Class Definition"""


class Square:
    """A simple class representing a square."""

    def __init__(self, size=0):
        """Initializes a new square with the given size."""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2
