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
