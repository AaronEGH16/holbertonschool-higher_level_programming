#!/usr/bin/python3
"""
this module contains "inherits_from" function
"""


def inherits_from(obj, a_class):
    """
    returns True if obj is an
    inherence of a_class

    Note:
        isinstance() returns True if obj is
            an instance of a_class and any parent
        issubcass() returns True if obj is
            a subclass of a_class
        type() return a exactly type of obj
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
