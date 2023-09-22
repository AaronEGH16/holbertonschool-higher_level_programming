#!/usr/bin/python3
def no_c(my_string):
    new_str = ''
    for c in my_string:
        if c != 'C' and c != 'c':
            new_str += c
    my_string = new_str
    return my_string
