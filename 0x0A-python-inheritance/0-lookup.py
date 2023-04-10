#!/usr/bin/python3
"""
simple function to return attributes and mehtods
"""


def lookup(obj):
    """function to return list of avilablee attributes and methods of an object
    Args:
        obj - instance of an object from a class
    """
    return dir(obj)
