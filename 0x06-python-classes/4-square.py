#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Represents a square with a specified size."""

    def __init__(self, size=0):
        """Initializes a new square with the given size."""

        self.size = size

    def area(self):
        """Calculates and returns the area of the square."""

        return self.size ** 2

    @property
    def size(self):
        """Getter method for the size attribute."""

        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size attribute."""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
