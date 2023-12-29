#!/usr/bin/python3

"""MyList class"""


class MyList(list):
    """MyList clast that inherits of list.

    Args:
        list (list): List as argument with all elements of type int.
    """
    def print_sorted(self):
        """Prints the list sorted (ascending sort)"""
        list_sorted = self.copy()
        list_sorted.sort()
        print(list_sorted)
