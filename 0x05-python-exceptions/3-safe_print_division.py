#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = int(a) / int(b)
        print("{:d} / {:d} = {:.1f}".format(a, b, result))
        return (result)
    except ZeroDivisionError:
        print("Error: Division by zero")
        return (None)
    finally:
        print("Inside finally block:")
        print("Inside result: {:.1f}".format(result))
