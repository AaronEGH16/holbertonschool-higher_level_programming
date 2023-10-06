#!/usr/bin/python3
"""
this module contains all info, methods and
functions of class "BaseGeometry"
"""


class BaseGeometry:
    """
    BaseGeometry Class

    methods:
        area()
        integer_validator()
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates integer values:

        name: always is a string
        value: verify if is integer and greater than 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
