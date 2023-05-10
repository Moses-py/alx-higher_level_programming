#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
abs_digit = abs(number) % 10
if abs_digit > 5:
    print(f"Last digit of {number:d} is {abs_digit:d} and is greater than 5")
elif abs_digit == 0:
    print(f"Last digit of {number:d} is {abs_digit:d} and is 0")
else:
    print(f"Last digit of {number:d} is {abs_digit:d} and is less than 6 and not 0")
