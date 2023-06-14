#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    if not my_list:
        return []
    else:
        return [my_list[0] * number] + multiply_list_map(my_list[1:], number)
