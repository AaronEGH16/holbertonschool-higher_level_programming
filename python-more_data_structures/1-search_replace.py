#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        new_list = []
        for x in my_list:
            if x != search:
                new_list.append(x)
            else:
                new_list.append(replace)
        return new_list
