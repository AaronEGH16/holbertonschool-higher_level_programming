#!/usr/bin/python3
"""

"""


def read_file(filename=""):
    """
    
    """
    with open(filename, "r", encoding="utf-8") as file:
        for f in file.read():
            print(f, end="")
