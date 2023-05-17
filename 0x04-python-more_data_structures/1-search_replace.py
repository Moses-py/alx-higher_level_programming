#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_arr = []
    for el in my_list:
        if el == search:
            list_arr.append(replace)
        else:
            list_arr.append(el)
    return list_arr
