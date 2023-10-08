#!/usr/bin/python3
"""
this module defines a 'pascal triangle' function
"""


def pascal_triangle(n):
    """
    this function get the size of
    pascal triangle and return
    list of list of integers
    representing it
    """
    if n <= 0:
        return []

    pas_tri = [[1]]

    if n == 1:
        return pas_tri

    while n > len(pas_tri):
        # create a new list of integers for new triangle level
        pas_tri.append([])
        x = 0
        while x < len(pas_tri):
            # insert in the actual level the integers
            # that represent a pascal triangle
            pas_tri[len(pas_tri) - 1].append(
                1 if (x == 0 or x == len(pas_tri) - 1) else
                (pas_tri[len(pas_tri) - 2])[x - 1] +
                (pas_tri[len(pas_tri) - 2])[x])
            # uses the previous list values to complete center of triangle
            x += 1

    return pas_tri
