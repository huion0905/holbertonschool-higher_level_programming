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

    def area(self):
        """Returns the area."""
        return self.__width * self.__height

    def __str__(self):
        """Return a informal string representation of the instance.

        Returns:
            str: String representatino of the instance
            using width and height attributes.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
