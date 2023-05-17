#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    numeral = 0
    item = 0

    for tuple in my_list:
        numeral += tuple[0] * tuple[1]
        item += tuple[1]

    return (numeral / item)
