#!/usr/bin/python3
"""
This Module contains definition of rectangle
"""


class Rectangle():
    """
    This class contains ojects that define a Rectangle
    """
    @property   # returns value of private instance __height
    def height(self):
        return self.__height

    @height.setter  # setter a new value to private instance __height
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property   # returns value of private instance __width
    def width(self):
        return self.__width

    @width.setter   # setter a new value to private instance __width
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def __init__(self, width=0, height=0):  # asign initial values to instances
        self.height = height
        self.width = width

    def area(self):  # returns area of rectangle
        return self.__height * self.__width

    def perimeter(self):  # returns perimeter of rectangle
        if self.__width != 0 and self.__height != 0:
            return (self.__height + self.__width) * 2
        else:
            return 0
