#!/usr/bin/python3
"""
This module contains the Rectangle class,
This class is inherited from the BaseGeometry class.
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class inherited from BaseGeometry class

    methods:
        __init__
        area()
        __str__
    """
    def __init__(self, width, height):
        """
        this method inicialize and check values of height and width
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        returns area of the Rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        returns a string representation of Rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
