#!/usr/bin/python3

"""print_square function"""


def print_square(size):
    """Prints the square using the size of the square

    Parameters:
        size (int): size of the square

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
        TypeError: If size if float and is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
