#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if len(my_list)<=idx or idx <0:
        return None
    else:
        my_list[idx] = element
        return my_list
