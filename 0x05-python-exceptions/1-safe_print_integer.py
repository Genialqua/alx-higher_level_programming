#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if str(value).isdigit():  # Check if value is a digit (after converting to string)
            print("value = {:d}".format(int(value)))  # Print value as integer
            return True
        else:
            return False
    except ValueError:
        print("Value is not a digit")
        return False
