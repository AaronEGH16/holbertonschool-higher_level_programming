#!/usr/bin/python3
"""
this module contains function matrix_divided
"""


def matrix_divided(matrix, div):
    """
    get a 'matrix' (list of lists) of numbers and return a matrix
    of result of all elements divided by 'div'
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list)) or (not isinstance(matrix[0], list)):
        raise TypeError(err)
    len_row = len(matrix[0])
    for row in matrix:
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(err)
        if len(row) != len_row:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )
    res = []
    for row in matrix:
        new_row = []
        for x in row:
            new_row.append(round(x / div, 2))
        res.append(new_row)
    return res
