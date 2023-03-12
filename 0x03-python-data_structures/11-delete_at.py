#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """deletes the item at a specified position
    Args:
        my_list: given list
        idx: index to delete
    Returns:
        new list after deleting element at idx
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
