#!/usr/bin/python3

"""Call base BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""Rectangle class"""


class Rectangle(BaseGeometry):
    """Defines a rectangle that inherits from BaseGeometry class."""
    def __init__(self, width, height):
        """
        Initialize the rectangle class
        validating width and height values.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
