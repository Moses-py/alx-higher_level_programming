#!/usr/bin/python3
"""Define a class-checker."""


def is_same_class(obj, a_class):
    """Check if object is instance of class.

    Args:
        obj (any): object to check.
        a_class (type): class to match type of obj to.
    Returns:
        If obj is exactly instance of a_class - True.
        else - False.
    """
    if type(obj) == a_class:
        return True
    return False
