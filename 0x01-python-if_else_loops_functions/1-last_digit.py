#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number >= 0:
    last_digit = number % 10
else:
    last_digit = number % -10

la_di = "Last digit of"
la_di1 = "and is less than 6 and not 0"

if last_digit > 5:
    print(la_di+" {} is {} and is greater than 5".format(number, last_digit))
elif last_digit == 0:
    print(la_di+" {} is {} and is 0".format(number, last_digit))
elif (last_digit < 6) and (last_digit != 0):
    print(la_di+" {} is {} ".format(number, last_digit) + la_di1)
