#!/usr/bin/python3
"""Square class module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defines the Square class."""

    def __init__(self, size):
        """Initialize the Square instance."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2
