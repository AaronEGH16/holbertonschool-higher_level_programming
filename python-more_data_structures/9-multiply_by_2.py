#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    for k in new_dic:
        new_dic.update({k: new_dic[k]*2})
    return new_dic
