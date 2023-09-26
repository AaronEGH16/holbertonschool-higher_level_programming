#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = list(a_dictionary.keys())
    sorted_keys.sort()
    sorted_dict = {i: a_dictionary[i] for i in sorted_keys}
    for x in sorted_dict:
        print("{}: {}".format(x, sorted_dict[x]))

#   for key, value in sorted(a_dictionary.items()):
#       print("{}: {}".format(key, value))
