#!/usr/bin/python3
"""check object is an instance of a specified class"""


def is_same_class(obj, a_class):
    """Returns True if object is an instance of a class"""

    if isinstance(obj, a_class):
        return True
    return False   
