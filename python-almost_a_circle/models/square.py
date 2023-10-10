#!/usr/bin/python3
"""
this module contains a definition
of sub 'Rectangle Class', 'Square'
and their methods and functions
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square Class:

    Inherited Attributes:
        id
        width
        height
        x
        y

    Public Attributes:
        None

    Inherited Methods:
        area(self)
        display(self)

    Public Methods:
        __init__(self, width, height, x=0, y=0, id=None)
        size - (getter and setter)
        __str__(self)
        update(self, *args, **kwargs)
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        This method initializes the square class object,
        assigns an id, size and position to the object by passing the values
        to the initialization function of the parent class.

        No need to pass the x and y arguments
        since its default value is 0
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        return string: [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """
        returns size of Square
        """
        return self.height

    @size.setter
    def size(self, size):
        """
        validates and asign size value to Square
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        get argument values and update square values with them
        """
        if args and len(args) != 0:
            for key in range(len(args)):
                if key == 0:
                    self.id = args[0]
                elif key == 1:
                    self.size = args[1]
                elif key == 2:
                    self.x = args[2]
                elif key == 3:
                    self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
