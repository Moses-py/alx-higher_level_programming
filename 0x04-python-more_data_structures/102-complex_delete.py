#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dict_keys = list(a_dictionary.keys())

    for dict_val in dict_keys:
        if value == a_dictionary.get(dict_val):
            del a_dictionary[dict_val]

    return (a_dictionary)

