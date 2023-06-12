#!/usr/bin/python3
"""Defines inherited class-checker."""


def inherits_from(obj, a_class):
    """Checks if object is inherited instance of class.

    Args:
        obj (any): object to check.
        a_class (type): class to match type of obj.
    Returns:
        If obj is inherited instance of a_class - True.
        rwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False