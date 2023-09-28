#!/usr/bin/python3
""" This module define a class Square """


class Square:
    """ This class define a Square of size = 'size'
    validating type and value; and adding function area"""
    def __init__(self, size=0, position=(0,0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ return value of Square position """
        return self.position

    @position.setter
    def position(self, value):
        """ Set the value of position passed by arguments """
        

    def my_print(self):
        """ print Square of area = 'area' by '#' """
        if self.__size > 0:
            for _ in range(self.__size):
                for _ in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
