#!/usr/bin/python3
"""
this module contains all test of rectangle module
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class RectangleClassTest(unittest.TestCase):
    """
    test of rectangle class:
        - test class inheritance
        - test rectangle id
        - test width get/set
        - test height get/set
        - test x get/set
        - test y get/set
        - test width TypeError
        - test height TypeError
        - test x TypeError
        - test y TypeError
        - test width ValueError
        - test height ValueError
        - test x ValueError
        - test y ValueError
        - test Area
    """
    def test_class_inheritance(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_rectangle_id(self):
        rectangle = Rectangle(5, 10, 0, 0, 20)
        self.assertEqual(rectangle.id, 20)

    def test_width_getset(self):
        rectangle = Rectangle(5, 10, 0, 0, 20)
        self.assertEqual(rectangle.width, 5)
        rectangle.width = 6
        self.assertEqual(rectangle.width, 6)

    def test_height_getset(self):
        rectangle = Rectangle(5, 10, 0, 0, 20)
        self.assertEqual(rectangle.height, 10)
        rectangle.height = 7
        self.assertEqual(rectangle.height, 7)

    def test_x_getset(self):
        rectangle = Rectangle(5, 10, 0, 0, 20)
        self.assertEqual(rectangle.x, 0)
        rectangle.x = 8
        self.assertEqual(rectangle.x, 8)

    def test_y_getset(self):
        rectangle = Rectangle(5, 10, 0, 0, 20)
        self.assertEqual(rectangle.y, 0)
        rectangle.y = 9
        self.assertEqual(rectangle.y, 9)

    def test_width_TypeError(self):
        with self.assertRaises(TypeError) as err:
            rectangle = Rectangle("Hola", 2, 3, 4)
            self.assertEqual(str(err.exception), "width must be an integer")

    def test_height_TypeError(self):
        with self.assertRaises(TypeError) as err:
            rectangle = Rectangle(1, "Hola", 3, 4)
            self.assertEqual(str(err.exception), "height must be an integer")

    def test_x_TypeError(self):
        with self.assertRaises(TypeError) as err:
            rectangle = Rectangle(1, 2, "Hola", 4)
            self.assertEqual(str(err.exception), "x must be an integer")

    def test_y_TypeError(self):
        with self.assertRaises(TypeError) as err:
            rectangle = Rectangle(1, 2, 3, "Hola")
            self.assertEqual(str(err.exception), "y must be an integer")

    def test_width_ValueError(self):
        with self.assertRaises(ValueError) as err:
            rectangle = Rectangle(0, 2, 3, 4)
            self.assertEqual(str(err.exception), "width must be > 0")

    def test_height_ValueError(self):
        with self.assertRaises(ValueError) as err:
            rectangle = Rectangle(1, 0, 3, 4)
            self.assertEqual(str(err.exception), "height must be > 0")

    def test_width_ValueError(self):
        with self.assertRaises(ValueError) as err:
            rectangle = Rectangle(-1, 2, 3, 4)
            self.assertEqual(str(err.exception), "width must be > 0")

    def test_height_ValueError(self):
        with self.assertRaises(ValueError) as err:
            rectangle = Rectangle(1, -2, 3, 4)
            self.assertEqual(str(err.exception), "height must be > 0")

    def test_x_ValueError(self):
        with self.assertRaises(ValueError) as err:
            rectangle = Rectangle(1, 2, -3, 4)
            self.assertEquals(str(err.exception), "x must be >= 0")

    def test_y_ValueError(self):
        with self.assertRaises(ValueError) as err:
            rectangle = Rectangle(1, 2, 3, -4)
            self.assertEqual(str(err.exception), "y must be >= 0")

    def test_Area(self):
        rectangle = Rectangle(2, 5)
        self.assertEqual(rectangle.area(), 10)
