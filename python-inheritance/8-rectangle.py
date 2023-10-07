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
    """
    def __init__(self, width, height):
        """
        this method inicialize and check values of height and width
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
