#!/usr/bin/python3
"""Defines a function that adds attrb to objects."""


def add_attribute(obj, att, value):
    """Add new attrb to object if possible.

    Args:
        obj (any): The object to add an attrb to.
        att (str): The name of the attrb to add to obj.
        value (any): The value of attrb.
    Raises:
        TypeError: If the attrb cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
