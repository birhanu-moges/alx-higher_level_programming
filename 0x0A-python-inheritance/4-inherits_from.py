#!/usr/bin/python3
"""check object is an instance of a specified class"""


def is_kind_of_class(obj, a_class):
    """Returns True if object is an instance of a class"""

    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
