#!/usr/bin/python3
"""
this module contains write file function
"""


def append_write(filename="", text=""):
    """
    this function write (append at the end of file)
    and return number of chars writed
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
