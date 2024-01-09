#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if len(my_list) <= idx or idx < 0:
        return my_list
    else:
        new_list = my_list[:]
        new_list[idx] = element
        print(new_list,new_list[idx])
        return new_list
