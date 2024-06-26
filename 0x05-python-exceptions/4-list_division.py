#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    l1 = len(my_list_1)
    l2 = len(my_list_2)
    new_list = []

    if list_length == l1 and list_length == l2:
        try:
            for a, b in zip(my_list_1, my_list_2):
                if isinstance(a, int) and isinstance(b, int):
                    result = a / b
                    new_list.append(result)
                else:
                    print("Wrong type")
                    return []
        except ZeroDivisionError:
            print("Division by zero")
            return []
        finally:
            print("Operation completed")
    else:
        print("Lists are not of equal length")

    return new_list
