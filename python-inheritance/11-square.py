#!/usr/bin/python3
"""
This module contains the Square class,
This class is inherited from the Rectangle class.
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square class inherited from Rectangle class

    methods:
        __init__
        __str__
    """
    def __init__(self, size):
        """
        initialize and verify size value of square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        returns a string representation of Square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
