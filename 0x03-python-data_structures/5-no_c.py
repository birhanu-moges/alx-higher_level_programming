#!/usr/bin/python3

def no_c(my_string):
    """Removes all characters C and c from string

    Args:
        my_string: given string to check for C and c

    Returns:
        new string whitout c and C
    """
    new_str = ""
    for str in my_string:
        if str != 'c' or str != 'C':
            new_str += str
    return new_str
