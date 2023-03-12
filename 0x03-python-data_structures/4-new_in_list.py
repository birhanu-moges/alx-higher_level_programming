#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replace an element of  a list at index idx and return new list

    Args:
        my_list: list argument
        idx: given index in the list
        element: new value to replace

        Returns:
            new list
    """
    new_list = []
    if my_list:
        for value in my_list:
            new_list.append(value)
    if idx < 0 or idx >= len(my_list):
        return new_list
    new_list[idx] = element
    return new_list
