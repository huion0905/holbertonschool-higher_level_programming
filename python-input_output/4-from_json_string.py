#!/usr/bin/python3

"""Call the json module"""
import json

"""Defines from_json_string function"""


def from_json_string(my_str):
    """Returns an object represented by a JSON string.

    Args:
        my_str (str): String to parse to JSON.

    Returns:
        obj: An object (Python data structure).
    """
    return json.loads(my_str)
