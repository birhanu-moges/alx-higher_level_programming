#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replace an element of  a list at index idx

    Args:
        my_list: list argument
        idx: given index in the list
        element: new value to replace

        Returns:
            element at index idx
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
