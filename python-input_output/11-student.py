#!/usr/bin/python3
"""
this module contains a definition of Student class
"""


class Student:
    """
    Strudent class:

    public atributes:
        first_name
        last_name
        age

    methods:
        __init__(self, first_name, last_name, age)
        to_json(self, attrs)
        reload_from_json(self, json)
    """

    def __init__(self, first_name, last_name, age):
        """
        this method initialize atributes of the class object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returns a serializable JSON dictionary of the object,
        filtering the elements
        """
        if (attrs is None) or (type(attrs) is not list):
            return self.__dict__
        dic = {}
        for element in self.__dict__.keys():
            if element in attrs:
                dic.update({element: (self.__dict__)[element]})
        return dic

    def reload_from_json(self, json):
        """
        load all object class elements from a JSON file
        """
        (self.__dict__).update(json)
