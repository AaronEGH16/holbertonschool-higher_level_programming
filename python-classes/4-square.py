#!/usr/bin/python3
""" This module define a class Square """


class Square:
    """ This class define a Square of size = 'size'
    validating type and value; and adding function area"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """ return value of Square size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the value of size passed vi arguments """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ return value of Square area """
        return self.__size * self.__size
    pass
