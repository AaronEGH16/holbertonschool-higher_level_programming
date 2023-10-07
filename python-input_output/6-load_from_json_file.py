#!/usr/bin/python3
"""
this module contains 'load from json file'
function, read JSON file and returns decoded string
"""
import json


def load_from_json_file(filename):
    """
    returns decoded JSON string file
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
