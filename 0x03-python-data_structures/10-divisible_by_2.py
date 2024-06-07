#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            print(f"{my_list[i]} is divisible by 2")
        elif my_list[i] % 2 != 0:
            print(f"{my_list[i]} is not divisible by 2")

