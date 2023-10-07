#!/usr/bin/python3
"""

"""
import sys
save_json = __import__("5-save_to_json_file").save_to_json_file
load_json = __import__("6-load_from_json_file").load_from_json_file

if __name__ == "__main__":
    filename = "add_item.json"
    list = []

    try:
        list.extend(load_json(filename))
    except FileNotFoundError:
        save_json([], filename)

    for element in sys.argv[1:]:
        list.append(element)

    save_json(list, filename)

    sys.exit(0)
