#!/usr/bin/python3
"""
this module contains to json string
function, this function returns a string representation of
an object
"""
import json


def to_json_string(my_obj):
    """
    return a JSON representation of an object
    """
    return json.dumps(my_obj)
