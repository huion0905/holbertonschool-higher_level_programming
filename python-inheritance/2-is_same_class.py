#!/usr/bin/python3

"""Define is_same_class function"""


def is_same_class(obj, a_class):
    """Checks if the object is exactly an instance of the specified class.

    Args:
        obj (obj): Object to be checked.
        a_class (class): Class to check.

    Returns:
        bool: True if object is an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
