#!/usr/bin/python3
"""
Module to wite an object to a text file using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """function to wite an object to a text file using JSON representation
    Args:
        my_obj: object
        filename: file name
    """
    text = json.dumps(my_obj)
    with open(filename, 'w') as fd:
        fd.write(text)
