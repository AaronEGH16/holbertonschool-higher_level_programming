#!/usr/bin/python3
"""
this module contains "is_same_class" function
"""


def is_same_class(obj, a_class):
    """
    returns True if obj is exactly an
    instance of a_class

    Note:
        isinstance() returns True if obj is
            an instance of a_class and any parent
        issublcass() returns True if obj is
            a subclass of a_class
        type() return a exactly type of obj
    """
    return type(obj) is a_class
