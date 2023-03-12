#!/usr/bin/python3

def no_c(my_string):
    """Removes all characters C and c from string

    Args:
        my_string: given string to check for C and c

    Returns:
        new string whitout c and C
    """
    idx = 0
    new_str = ""
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            new_str += my_string[i]
    return new_str
