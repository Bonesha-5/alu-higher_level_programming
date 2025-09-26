#!/usr/bin/python3
"""
This module prints a square.
"""

def print_square(size):
    """
    Prints a square using '#' of given size.

    Args:
        size: int (size of square)

    Raises:
        TypeError, ValueError
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
