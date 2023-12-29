#!/usr/bin/python3

"""Square class"""


class Square:
    """Class representing a square"""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int, optional): size of the square. Defaults to 0.

        Raises:
            TypeError: If size if not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: area of the square.

        """
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square using '#' character"""
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)
