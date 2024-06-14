#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set()  # Use a set instead of a dictionary
    for element in set_1:
        if element not in set_2:
            new_set.add(element)
    for element in set_2:
        if element not in set_1:
            new_set.add(element)
    return (new_set)
