#!/usr/bin/python3
"""
this module contains a
definition of 'Base Class'
and their methods and functions
"""
import json
import turtle


class Base:
    """
    Base Class:

    Public Attributes:
        id

    Methods:
        __init__(self, id=None)
    Static Methods:
        to_json_string(list_dictionaries)
        from_json_string(json_string)
        draw(list_rectangles, list_squares)
    Class Methods:
        save_to_file(cls, list_objs)
        create(cls, **dictionary)
        load_from_file(cls)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        This method initializes a base class object
        and assigns an id (it is always an integer).

        If the id argument is not passed,
        the new id is the base class object number.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        return a JSON string representation of dictionaries
        """
        if (list_dictionaries is None) or (len(list_dictionaries) == 0):
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        create a class JSON file to save a class objects
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as file:
            dict = []
            if list_objs is not None:
                for objs in list_objs:
                    dict.append(cls.to_dictionary(objs))
            file.write(cls.to_json_string(dict))

    @staticmethod
    def from_json_string(json_string):
        """
        convert JSON string to list of elements
        """
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        check the class and if the dictionary is not None,
        create a Class object using the dictionary data
        """
        if cls is not Base and\
                (dictionary and dictionary != {}):
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """
        method to load a class object from a JSON class file
        """
        filename = "{}.json".format(cls.__name__)
        obj_list = []
        try:
            with open(filename, "r") as file:
                class_object = cls.from_json_string(file.read())
            for key in range(len(class_object)):
                obj_list.append(cls.create(**class_object[key]))
        except FileNotFoundError:
            pass
        return obj_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw all Rectangles and Squares from the lists using the turtle module.
        """
        draw_turt = turtle.Turtle()
        draw_turt.screen.bgcolor("#000000")
        draw_turt.pensize(1)
        draw_turt.shape("turtle")

        draw_turt.color("#49B43A")
        for rectangle in list_rectangles:
            draw_turt.showturtle()
            draw_turt.up()
            draw_turt.goto(rectangle.x, rectangle.y)
            draw_turt.down()
            for i in range(2):
                draw_turt.fd(rectangle.width)
                draw_turt.lt(90)
                draw_turt.fd(rectangle.height)
                draw_turt.lt(90)
            draw_turt.hideturtle()

        draw_turt.color("#1FBBE1")
        for square in list_squares:
            draw_turt.showturtle()
            draw_turt.up()
            draw_turt.goto(square.x, square.y)
            draw_turt.down()
            for i in range(2):
                draw_turt.fd(square.width)
                draw_turt.lt(90)
                draw_turt.fd(square.height)
                draw_turt.lt(90)
            draw_turt.hideturtle()

        turtle.exitonclick()
