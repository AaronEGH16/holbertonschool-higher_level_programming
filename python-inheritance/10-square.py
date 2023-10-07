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
    """
    def __init__(self, size):
        """
        initialize and verify size value of square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
