#!/usr/bin/python3

"""Call base Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


"""Square class"""


class Square(Rectangle):
    """Defines a square that inherits from Rectangle class."""
    def __init__(self, size):
        """
        Initialize the square class
        validating size value.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area."""
        return self.__size ** 2
