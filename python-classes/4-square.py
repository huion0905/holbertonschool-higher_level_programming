#!/usr/bin/python3

"""Square class"""


class Square:
    """Defines a empty square class."""
    def __init__(self, size=0):
        """Instance initialization
        Attributes:
            size: size of square. """
        self.__size = size

    @property
    def size(self):
        """ Retrieve the size of the square.
        Returns:
            int: size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of the square.
        Args:
            value (int): size to set.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Calculate and return the area of the square.
        Returns:
            int: area of the square.
        """
        return self.__size ** 2
