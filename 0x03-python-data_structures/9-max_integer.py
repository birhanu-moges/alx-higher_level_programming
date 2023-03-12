#!/usr/bin/python3

def max_integer(my_list=[]):
    """Find the bigest integer of a list
    Args:
        my_list: list to check
    Returns:
        the max value of a list
    """
    if len(my_list) == 0:
        return None
    tmp = my_list[0]
    for element in my_list:
        if tmp < element:
            tmp = element
    return tmp
