#!/usr/bin/python3
"""
this module contains write file function
"""


def write_file(filename="", text=""):
    """
    this function write (re write an existent file)
    and return number of chars writed
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
