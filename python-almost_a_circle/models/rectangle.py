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

    Inherited Attributes:
        id

    Public Attributes:
        None

    Public Methods:
        __init__(self, width, height, x=0, y=0, id=None)
        width - (getter and setter)
        height - (getter and setter)
        x - (getter and setter)
        y - (getter and setter)
        area(self)
        display(self)
        __str__(self)
        update(self, *args, **kwargs)
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

    def area(self):
        """
        returns the result of the area calculation of the rectangle
        """
        return self.height * self.width

    def display(self):
        """
        print a visual respresentation of the Rectangle
        """
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """
        print [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        get argument values and update rectangle values with them
        """
        if args:
            for key in range(len(args)):
                if key == 0:
                    self.id = args[0]
                elif key == 1:
                    self.width = args[1]
                elif key == 2:
                    self.height = args[2]
                elif key == 3:
                    self.x = args[3]
                elif key == 4:
                    self.y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
