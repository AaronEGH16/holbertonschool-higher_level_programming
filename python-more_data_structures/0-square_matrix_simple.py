#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        square_matrix = []
        for x in matrix:
            square_matrix.append(list(map(lambda x: x**2, x)))
        return square_matrix
