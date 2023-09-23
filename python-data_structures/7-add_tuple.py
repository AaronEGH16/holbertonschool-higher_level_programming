#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > 0:
        num1 = tuple_a[0]
    else:
        num1 = 0
    if len(tuple_b) > 0:
        num1 += tuple_b[0]
    
    if len(tuple_a) > 1:
        num2 = tuple_a[1]
    else:
        num2 = 0
    if len(tuple_b) > 1:
        num2 += tuple_b[1]
    
    new_tuple=(num1, num2)
    return new_tuple

