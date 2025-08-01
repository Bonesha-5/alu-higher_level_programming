#!/usr/bin/python3
"""
This module adds two integers.
"""

def add_integer(a, b=98):
    """
    Returns the integer addition of a and b.

    Args:
        a: int or float
        b: int or float (default 98)

    Raises:
        TypeError: if a or b is not an int or float

    Returns:
        int: sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

