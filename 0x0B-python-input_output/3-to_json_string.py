#!/usr/bin/python3
"""
Module to return JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """function to rerurn JSON representaion of an object
    Args:
        my_obj: object
    """
    return json.dumps(my_obj)
