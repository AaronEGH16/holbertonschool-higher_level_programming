#!/usr/bin/python3
"""
this module contains a definition of Student class
"""


class Student:
    """
    Strudent class:

    atributes:
        first_name
        last_name
        age

    methods:
        __init__(self, first_name, last_name, age)
        to_json(self)
    """

    def __init__(self, first_name, last_name, age):
        """
        this method initialize atributes of the class object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        return a JSON serializable dictionary of object
        """
        return self.__dict__
