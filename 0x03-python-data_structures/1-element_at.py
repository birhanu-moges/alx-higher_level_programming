#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrieves an element from a list at index idx

    Args:
        my_list: list argument
        idx: given index in the list

        Returns:
            element at index idx
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
