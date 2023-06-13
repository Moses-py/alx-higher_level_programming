#!/usr/bin/python3
"""Define class Student."""


class Student:
    """Represent student."""

    def __init__(self, first_name, last_name, age):
        """Initialize new Student.

        Args:
            first_name (str): first name of student.
            last_name (str): last name of student.
            age (int): age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of Student.

        If attrs is a list of strings, represents only those attributes
        included in list.

        Args:
            attrs (list): (Optional) attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of Student.

        Args:
            json (dict): key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
