#!/usr/bin/python3
"""
This Module contains definition of rectangle
"""


class Rectangle():
    """
    This class contains ojects that define a Rectangle
    """

    def __init__(self, width=0, height=0):  # asign initial values to instances
        self.height = height
        self.width = width
        type(self).number_of_instances += 1  # increment global counter

    number_of_instances = 0  # public class value counter
    print_symbol = "#"  # public class symbol representation

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

    def area(self):  # returns area of rectangle
        return self.__height * self.__width

    def perimeter(self):  # returns perimeter of rectangle
        if self.__width != 0 and self.__height != 0:
            return (self.__height + self.__width) * 2
        else:
            return 0

    def __str__(self) -> str:  # representation of rectangle for final user
        """
        join insert '\n' after time iteration of for
        and return the completed rectangle of variable
        'print_symbol' in form of text
        """
        if self.__width != 0 and self.__height != 0:
            return "\n".join([str(self.print_symbol) * self.__width
                              for _ in range(self.__height)])
        else:
            return ""

    def __repr__(self) -> str:  # representation of rectangle for programmer
        """
        returns a string representation of rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):  # prints message when an object or reference is deleted
        type(self).number_of_instances -= 1  # decrese global counter
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        this method compare area of two rectangles
        and returns the bigger of them
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        bigger = (lambda x, y: x if x.area() >= y.area() else y)
        return bigger(rect_1, rect_2)

    @classmethod
    def square(cls, size=0):
        """
        defines a class method square to create a
        rectangule of size * size and return it
        """
        return cls(size, size)
