#!/usr/bin/python3
"""Define a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int opps == and !=."""

    def __eq__(self, value):
        """replace == opps with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """replace != opp with == behavior."""
        return self.real == value
