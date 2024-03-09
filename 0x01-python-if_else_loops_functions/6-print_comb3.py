#!/usr/bin/python3

for i in range(1, 90):
    if i < 10:
        print("0{:d}".format(i), end=", ")
    elif i > 9 and i != 89:
        print("{:d}".format(i), end=", ")
    else:
        print("{:d}".format(i))
