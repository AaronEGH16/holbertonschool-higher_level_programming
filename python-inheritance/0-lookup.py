#!/usr/bin/python3
"""
this module contains lookup function
"""


def lookup(obj):
    """
    lookup function gets a obj and return a list
    of all available attributes and methods of them
    """
    return dir(obj)
