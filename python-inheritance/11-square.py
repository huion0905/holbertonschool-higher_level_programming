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
        super().__init__(self.__size, self.__size)

    def area(self):
        """Returns the area."""
        return super().area()

    def __str__(self):
        """Return a informal string representation of the instance.

        Returns:
            str: String representatino of the instance
            using size attribute.
        """
        return f"[Square] {self.__size}/{self.__size}"
