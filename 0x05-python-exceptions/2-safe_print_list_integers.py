#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        new_list = my_list[:x]  # Get sublist up to index x (not including x itself)
        int_list = []  # List to store integers from new_list
        count = 0  # Initialize count for printing

        for e in new_list:
            if isinstance(e, int):  # Check if element is an integer
                int_list.append(e)  # Append integer to int_list

        for f in int_list:
            try:
                print("{:d}".format(f))  # Print integer with formatting
                count += 1
            except ValueError:
                print("ValueError: Cannot format as integer")

    except IndexError:
        print("Out of range")
