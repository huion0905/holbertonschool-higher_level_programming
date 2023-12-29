#!/usr/bin/python3

"""add_integer function"""


def add_integer(a, b=98):
    """Adds 2 integer numbers.

    Parameters:
        a (int or float): first number.
        b (int or float, optional): second number. Defaults to 98.

    Raises:
        TypeError: If a and b are not integers or floats.

    Returns:
        int: the addition of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
