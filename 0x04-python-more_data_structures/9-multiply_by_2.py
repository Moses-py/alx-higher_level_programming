#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    update_dictionary = {}
    for item, val in a_dictionary.items():
        update_dictionary.update({item: (val * 2)})
    return update_dictionary
