#!/usr/bin/python3
"""
Module to create an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """function to create an Object from a “JSON file"
    Args:
        filename: file name
    """
    with open(filename, 'r') as fd:
        json.load(fd)
