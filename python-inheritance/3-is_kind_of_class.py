#!/usr/bin/python3
"""
this module contains "is_kind_of_class" function
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if obj is an
    instance of a_class or inherence

    Note:
        isinstance() returns True if obj is
            an instance of a_class and any parent
        issublcass() returns True if obj is
            a subclass of a_class
        type() return a exactly type of obj
    """
    return isinstance(obj, a_class)
