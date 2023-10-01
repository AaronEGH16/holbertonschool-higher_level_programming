#!/usr/bin/python3
"""
get string and print whit indentation
"""


def text_indentation(text):
    """ print text whit \n after '. or ? or :' """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    prev = False
    for ch in text:
        if prev == True:
            prev = False
            continue
        print("{}".format(ch), end="")
        if ch == "." or ch == "?" or ch == ":":
            print("{}".format("\n"))
            prev = True
