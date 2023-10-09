#!/usr/bin/python3
"""
this module contains a
definition of 'Base Class'
and their methods and functions
"""


class Base:
    """
    Base Class:

    Public Attributes:
        id

    Public Methods:
        __init__(self, id=None)
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
