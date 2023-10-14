#!/usr/bin/python3
"""
this module contains all test of base module
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class BaseClassTest(unittest.TestCase):
    """
    tests of base class:
        - id
        - private var increment
        - to json (None)
        - to json (empty)
        - to json (correct)
    """
    def test_Id(self):
        obj = Base(20)
        self.assertEqual(obj.id, 20)

    def test_Private_nb_objects_increment(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_to_json_None(self):
        js_string = Base.to_json_string(None)
        self.assertEqual("[]", js_string)

    def test_to_json_Empty(self):
        js_string = Base.to_json_string([])
        self.assertEqual("[]", js_string)

    def test_to_json_Correct(self):
        correct = '[{"id": 20, "width": 15, "height": 8, "x": 5, "y": 3}]'
        rectangle = Rectangle(15, 8, 5, 3, 20)
        rec_dic = rectangle.to_dictionary()
        dic_of_rec = [rec_dic]
        js_string = Base.to_json_string(dic_of_rec)
        self.assertEqual(correct, js_string)
