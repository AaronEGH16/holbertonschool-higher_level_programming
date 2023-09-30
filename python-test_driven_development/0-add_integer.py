#!/usr/bin/python3
"""
this module contains function add,
recibe 2 ints elements and returns add of them
>>> add_integer(7, 3)
3
"""


def add_integer(a, b=98):
    """
    sum int or float A & B and return int result
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
