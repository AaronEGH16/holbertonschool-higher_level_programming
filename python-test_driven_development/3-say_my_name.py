#!/usr/bin/python3
"""
this module contains the say_my_name function,
recive 2 strings arguments and print:
My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    this function print full name passed by arguments
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
