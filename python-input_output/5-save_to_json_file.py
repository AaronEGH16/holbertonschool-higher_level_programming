#!/usr/bin/python3
"""
this module contains 'save to json file'
that save a JSON string encoding in a
new or re writed file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    this function create a JSON string representation and wriet it into file
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
