#!/usr/bin/python3

import sys


def add_arguments(*args):
    total = 0
    for arg in args:
        total += int(arg)
    return (total)


if __name__ == "__main__":
    args = sys.argv[1:]
    result = add_arguments(*args)
    print(result)
