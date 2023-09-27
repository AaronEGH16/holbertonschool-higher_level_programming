#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for c in range(x):
        try:
            print("{}".format(my_list[c]), end="")
            count += 1
        except:
            break
    print()
    return count
