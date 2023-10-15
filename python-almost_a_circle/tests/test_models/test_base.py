#!/usr/bin/python3
"""
this module contains all test of base module
"""
import unittest
import json
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
        - from json (None)
        - from json (empty)
        - from json (correct)
        - save to file (None)
        - save to file (empty)
        - save to file (correct)
        - create
        - load from (None)
        - load from (empty)
        - load from (correct)
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

    def test_from_json_none(self):
        js = None
        lis_dic = Base.from_json_string(js)
        self.assertTrue(type(lis_dic) == list)
        self.assertTrue(lis_dic == [])

    def test_from_json_empty(self):
        js = ""
        lis_dic = Base.from_json_string(js)
        self.assertTrue(type(lis_dic) == list)
        self.assertTrue(lis_dic == [])

    def test_from_json_correct(self):
        js = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},\
               {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]'
        lis_dic = Base.from_json_string(js)
        self.assertTrue(type(js) == str)
        self.assertTrue(type(lis_dic) == list)
        self.assertTrue(type(lis_dic[0]) == dict)
        self.assertTrue(lis_dic,
                        [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
                         {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}])
        self.assertTrue(lis_dic[0],
                        {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5})

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_save_to_file_correct(self):
        r1 = Rectangle(5, 10, 1, 1, 20)
        r2 = Rectangle(6, 11, 2, 2, 21)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                json.dumps([r1.to_dictionary(), r2.to_dictionary()]),
                file.read())

    def test_create(self):
        r1 = Rectangle(3, 5, 1, 2, 99)
        r1_dic = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dic)
        self.assertEqual(str(r1), '[Rectangle] (99) 1/2 - 3/5')
        self.assertEqual(str(r2), '[Rectangle] (99) 1/2 - 3/5')
        self.assertIsNot(r1, r2)

    def test_load_from_none(self):
        Rectangle.save_to_file(None)
        list_dic = Rectangle.load_from_file()
        self.assertEqual(type(list_dic), list)
        self.assertEqual(len(list_dic), 0)

    def test_load_from_empty(self):
        Rectangle.save_to_file([])
        list_dic = Rectangle.load_from_file()
        self.assertEqual(type(list_dic), list)
        self.assertEqual(len(list_dic), 0)

    def test_load_from_correct(self):
        r1 = Rectangle(10, 7, 2, 8, 99)
        r2 = Rectangle(2, 4, 2, 2, 98)
        Rectangle.save_to_file([r1, r2])
        list_dic = Rectangle.load_from_file()
        self.assertEqual(len(list_dic), 2)
        for key in range(len(list_dic)):
            if key == 0:
                self.assertEqual(str(list_dic[key]), '[Rectangle] (99) 2/8 - 10/7')
            if key == 1:
                self.assertEqual(str(list_dic[key]), '[Rectangle] (98) 2/2 - 2/4')
