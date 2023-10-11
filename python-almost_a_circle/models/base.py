#!/usr/bin/python3
"""
this module contains a
definition of 'Base Class'
and their methods and functions
"""
import json


class Base:
    """
    Base Class:

    Public Attributes:
        id

    Public Methods:
        __init__(self, id=None)
        to_json_string(list_dictionaries)
        save_to_file(cls, list_objs)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        This method initializes a base class object
        and assigns an id (it is always an integer).

        If the id argument is not passed,
        the new id is the base class object number.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        return a JSON string representation of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
        return json.dumps(list_dictionaries)
