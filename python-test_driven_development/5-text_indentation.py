#!/usr/bin/python3
"""
get string and print whit indentation
"""


def text_indentation(text):
    r""" print text whit \n after '. or ? or :' """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = text.replace(". ", ".\n\n")\
        .replace("? ", "?\n\n").replace(": ", ":\n\n")
    print(new_text, end="")
