#!/usr/bin/python3

"""Rectangle class"""


class Rectangle:
    """Defines a rectangle

    Attributes:
        __width (int): Width of the rectangle.
        __height (int): Height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance.

        Args:
            width (int): Width of the rectangle. Defaults to 0.
            height (int): Height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle.

        Returns:
            int: width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): Width to set.

        Raises:
            TypeError: If value is not an integer.
            TypeValue: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle.

        Returns:
            int: height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): Height to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and return the perimeter of the rectangle.

        Returns:
            int: Perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)
        return perimeter

    def __str__(self):
        """Return an informal string representation of the rectangle.

        Returns:
            str: String representation of the rectangle using '#'
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        return '\n'.join('#' * self.__width for _ in range(self.__height))
