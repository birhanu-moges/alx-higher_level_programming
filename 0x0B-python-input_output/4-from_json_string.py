#!/usr/bin/python3
"""
Module to return an object form JSON representation
"""
import json


def from_json_string(my_str):
    """function to rerurn an object representaion JSON string
    Args:
        my_str: JSON String
    """
    return json.loads(my_str)
