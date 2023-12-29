#!/usr/bin/python3

"""read_file function"""


def read_file(filename=""):
    """Prints in stdout the content of filename.

    Args:
        filename (file): File to print it's content.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
