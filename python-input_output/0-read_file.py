#!/usr/bin/python3
"""
this module contains a read file function
"""


def read_file(filename=""):
    """
    function to read a file content and print it in standar output
    """
    with open(filename, "r", encoding="utf-8") as file:
        for f in file.read():
            print(f, end="")
