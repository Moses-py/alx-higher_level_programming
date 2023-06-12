#!/usr/bin/python3
"""
MyList class
"""


class MyList(list):
    """subclass of a list"""
    def __init__(self):
        """initialize object"""
        super().__init__()

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
