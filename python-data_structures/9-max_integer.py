#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list and len(my_list) > 0:
        max = my_list[0]
        for x in my_list:
            if x > max:
                max = x
    else:
        return None
    return max
