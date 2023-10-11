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

    Methods:
        __init__(self, id=None)
    Static Methods:
        to_json_string(list_dictionaries)
    Class Methods:
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        return a JSON string representation of dictionaries
        """
        if (list_dictionaries is None) or (len(list_dictionaries) == 0):
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        create a class JSON file to save a class objects
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as file:
            dict = []
            if (list_objs is not None) or (len(list_objs) != 0):
                for objs in list_objs:
                    dict.append(cls.to_dictionary(objs))
            file.write(cls.to_json_string(dict))
