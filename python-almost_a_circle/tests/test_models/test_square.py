#!/usr/bin/python3
"""
this module contains all test of square module
"""
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class SquareClassTest(unittest.TestCase):
    """
    test of square class:
        - test class inheritance
        - test square id
        - test size get/set
        - test x get/set
        - test y get/set
        - test size TypeError
        - test x TypeError
        - test y TypeError
        - test size ValueError
        - test x ValueError
        - test y ValueError
        - test Area
        - test __str__
        - test display
        - test update
        - test to dictionary
    """
    def test_class_inheritance(self):
        self.assertTrue(issubclass(Square, Base))

    def test_class_inheritance(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_square_id(self):
        square = Square(5, 0, 0, 20)
        self.assertEqual(square.id, 20)

    def test_size_getset(self):
        square = Square(5, 0, 0, 20)
        self.assertEqual(square.size, 5)
        square.size = 6
        self.assertEqual(square.size, 6)

    def test_x_getset(self):
        square = Square(5, 0, 0, 20)
        self.assertEqual(square.x, 0)
        square.x = 8
        self.assertEqual(square.x, 8)

    def test_y_getset(self):
        square = Square(5, 0, 0, 20)
        self.assertEqual(square.y, 0)
        square.y = 9
        self.assertEqual(square.y, 9)

    def test_size_TypeError(self):
        with self.assertRaises(TypeError) as err:
            square = Square("Hola", 2, 3)
            self.assertEqual(str(err.exception), "width must be an integer")

    def test_x_TypeError(self):
        with self.assertRaises(TypeError) as err:
            square = Square(1, "Hola", 3)
            self.assertEqual(str(err.exception), "x must be an integer")

    def test_y_TypeError(self):
        with self.assertRaises(TypeError) as err:
            square = Square(1, 2, "Hola")
            self.assertEqual(str(err.exception), "y must be an integer")

    def test_size_ValueError(self):
        with self.assertRaises(ValueError) as err:
            square = Square(0, 2, 3)
            self.assertEqual(str(err.exception), "width must be > 0")

    def test_size_ValueError(self):
        with self.assertRaises(ValueError) as err:
            square = Square(-1, 2, 3)
            self.assertEqual(str(err.exception), "width must be > 0")

    def test_x_ValueError(self):
        with self.assertRaises(ValueError) as err:
            square = Square(1, -2, 3)
            self.assertEquals(str(err.exception), "x must be >= 0")

    def test_y_ValueError(self):
        with self.assertRaises(ValueError) as err:
            square = Square(1, 2, -3)
            self.assertEqual(str(err.exception), "y must be >= 0")

    def test_Area(self):
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_str(self):
        square = Square(5, 1, 3, 20)
        self.assertEqual(square.__str__(), "[Square] (20) 1/3 - 5")

    def test_display(self):
        with StringIO() as buf, redirect_stdout(buf):
            Square(5).display()
            b = buf.getvalue()
        self.assertEqual(b, '#####\n#####\n#####\n#####\n#####\n')

    def test_update_args(self):
        square = Square(1, 1, 1, 10)
        square.update(20, 3, 0, 0)
        self.assertEqual(square.__str__(), "[Square] (20) 0/0 - 3")

    def test_update_kwargs(self):
        square = Square(1, 1, 1, 10)
        square.update(x=0, size=2, y=0, id=20)
        self.assertEqual(square.__str__(), "[Square] (20) 0/0 - 2")

    def test_to_dictionary(self):
        square = Square(5, 1, 1, 20)
        res = {'x': 1, 'y': 1, 'id': 20, 'size': 5}
        self.assertEqual(square.to_dictionary(), res)
