#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    (idx >= 0 and idx < len(my_list)) and my_list.__setitem__(idx, element)
    return my_list
