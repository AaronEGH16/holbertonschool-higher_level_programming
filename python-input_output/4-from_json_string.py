#!/usr/bin/python3
"""
this module contains 'form json string'
function, this function returns a decoding
JSON string
"""
import json


def from_json_string(my_str):
    """
    return a JSON decoding representation of an string
    """
    return json.loads(my_str)
