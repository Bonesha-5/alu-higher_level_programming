#!/usr/bin/python3
"""
This module divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements by div and returns a new matrix.

    Args:
        matrix: list of lists of int/float
        div: number to divide by

    Returns:
        New matrix with values rounded to 2 decimal places

    Raises:
        TypeError, ZeroDivisionError
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(el / div, 2) for el in row] for row in matrix]

