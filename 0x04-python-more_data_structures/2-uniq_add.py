#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_arr = []
    sum = 0
    for item in my_list:
        if item not in list_arr:
            sum += item
            list_arr.append(item)
    return sum
