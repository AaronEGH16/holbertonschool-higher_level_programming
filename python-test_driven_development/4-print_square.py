#!/usr/bin/python3
"""
this module contains definition of print square function
"""


def print_square(size):
    """ print a square of size * size """
    if not isinstance(size, int) or \
        (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")
    
    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
