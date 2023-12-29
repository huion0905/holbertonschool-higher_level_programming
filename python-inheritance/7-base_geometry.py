#!/usr/bin/python3

"""BaseGeometry class"""


class BaseGeometry:
    """Defines a base geometry"""
    def area(self):
        """Raises an Exception indicating that
        the area() method is not implemented.

        Raises:
            Exception: raises the Exception with the
            message "area() is not implemented."
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value argument.

        Args:
            name (str): An string as argument.
            value (int): An integer as argument

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less or equal to 0.
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
