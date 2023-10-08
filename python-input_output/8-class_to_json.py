#!/usr/bin/python3
"""
this module contains function to return a
dictionary of class elements for JSON serialization
of an object
"""
import json


def class_to_json(obj):
    """
    returns a dictionary of class elements
    to JSON serialization
    """
    return obj.__dict__
