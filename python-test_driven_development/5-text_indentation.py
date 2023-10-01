#!/usr/bin/python3
"""
get string and print whit indentation
"""


def text_indentation(text):
    """ print text whit \n after '. or ? or :' """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = text.replace(". ", ".")\
        .replace("? ", "?").replace(": ", ":")

    if new_text[0] == ' ':
        flag = True
    else:
        flag = False
    for ch in new_text:
        if ch == '?' or ch == '.' or ch == ':':
            print(ch)
            print()
            flag = True
            continue
        if flag is False:
            print(ch, end="")
            if ch == ' ':
                flag = True
        else:
            if ch != ' ':
                print(ch, end="")
                flag = False
