#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """print list in reversed order

    Args:
        my_list: list argument

    """
    if my_list:
        idx = len(my_list)-1
        for i in range(idx, -1, -1):
            print('{:d}'.format(my_list[i]))
