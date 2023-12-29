#!/usr/bin/python3

"""say_my_name function"""


def say_my_name(first_name, last_name=""):
    """Prints "My name is <first_name> <last_name>"

    Parameters:
        first_name (str): first_name to print
        last_name (str): last_name to print

    Returns:
        nothing
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
