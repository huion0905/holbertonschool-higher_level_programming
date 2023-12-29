#!/usr/bin/python3

"""Define the lookup function"""


def lookup(obj):
    """Returns a list object with all attributes and methods.

    Args:
        obj (obj): Object as argument to

    Returns:
        list (obj): Returns a list object.
    """
    return dir(obj)
