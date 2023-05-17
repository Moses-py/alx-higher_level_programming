#!/usr/bin/python3
def to_subtract(list_num):
    sub = 0
    max_list = max(list_num)

    for n in list_num:
        if max_list > n:
            sub += n

    return (max_list - sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    r_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(r_numerals.keys())

    numeral = 0
    prev_numeral = 0
    list_num = [0]

    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if r_numerals.get(ch) <= prev_numeral:
                    numeral += to_subtract(list_num)
                    list_num = [r_numerals.get(ch)]
                else:
                    list_num.append(r_numerals.get(ch))

                prev_numeral = r_numerals.get(ch)

    numeral += to_subtract(list_num)

    return (numeral)

