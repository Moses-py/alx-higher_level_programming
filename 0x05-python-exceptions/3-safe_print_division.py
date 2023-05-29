#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        enum = a / b
    except (TypeError, ZeroDivisionError):
        enum = None
    finally:
        print("Inside result: {}".format(enum))
    return (enum)
