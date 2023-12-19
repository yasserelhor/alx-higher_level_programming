#!/usr/bin/python3
"""Defines a Square class that represents a square."""


class Square:
    """Class for representing a square."""

    def __init__(self, size=0):
        """Initialize the square."""

        self.size = size

    @property
    def size(self):
        """int: Private size of the square."""

        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""

        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Calculate and return the area of the square."""

        return self.__size**2

    def my_print(self):
        """Print the square using the '#' character to stdout."""

        if self.__size != 0:
            for _ in range(self.__size):
                print('#' * self.__size)
        else:
            print()
