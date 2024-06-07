#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)

    if my_list != []:
        sort_list = sorted(my_list)
        return (sort_list[length-1])
    else:
        return (None)
