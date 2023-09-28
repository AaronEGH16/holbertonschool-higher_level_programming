#!/usr/bin/python3
""" This module define a class Square """


class Square:
    """ This class define a Square of size = 'size'
    validating type and value; and adding function area"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        print(f"{self.__size}")
        return self.__size * self.__size
    pass
