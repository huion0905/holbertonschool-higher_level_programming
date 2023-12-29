#!/usr/bin/python3

"""Define inherits_from function"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class,
    Args:
        obj (obj): Object to be checked.
        a_class (class): Class specified.

    Returns:
        bool: True if object is an instance of a_class inherited,
              otherwise False.
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
