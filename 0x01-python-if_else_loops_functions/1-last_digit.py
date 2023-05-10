#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
abs_digit = abs(number) % 10
if number < 0:
    abs_digit = -abs_digit
prefix = f"Last digit of {number:d} is {abs_digit:d} and is"
if abs_digit > 5:
    print(f"{prefix} greater than 5")
elif abs_digit == 0:
    print(f"{prefix} 0")
else:
    print(f"{prefix} less than 6 and not 0")
