#!/usr/bin/python3
"""This module defines a function that returns
the list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of stf attributes and methods.
    """
    return dir(obj)
