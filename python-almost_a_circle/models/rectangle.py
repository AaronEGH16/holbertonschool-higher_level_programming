#!/usr/bin/python3
"""
this module contains a definition
of sub 'Base Class', 'Rectangle'
and their methods and functions
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle Class:

    Inherited attributes:
        id

    Public attributes:

    Private attributes:
        __width
        __height
        __x
        __y

    Methods:
        __init__(self, width, height, x=0, y=0, id=None)
        width - (getter and setter)
        height - (getter and setter)
        x - (getter and setter)
        y - (getter and setter)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This method initializes the rectangle class object,
        assigns an id to the object using the initialize function
        of the parent class and uses the arguments width, height, x and y
        for the properties of the rectangle.

        It is not necessary to pass the arguments x and y
        since their value pre defined is 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        returns width of Rectangle
        """
        return self.__width

    @property
    def height(self):
        """
        returns height of Rectangle
        """
        return self.__height

    @property
    def x(self):
        """
        returns x position of Rectangle
        """
        return self.__x

    @property
    def y(self):
        """
        returns y position of Rectangle
        """
        return self.__y

    @width.setter
    def width(self, width):
        """
        validates and asign width value to Rectangle
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """
        validates and asign height value to Rectangle
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """
        validates and assigns the position value x to the Rectangle
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """
        validates and assigns the position value y to the Rectangle
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
