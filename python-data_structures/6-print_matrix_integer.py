#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for x in matrix:
            for y in x:
                if y != x[(len(x) - 1)]:
                    print("{:d}".format(y), end=" ")
                else:
                    print("{:d}".format(y), end="")
            print()
