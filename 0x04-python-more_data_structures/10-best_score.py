#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        new_list = list(a_dictionary.keys())
        score = 0
        top_pos = ""
        for i in new_list:
            if a_dictionary[i] > score:
                score = a_dictionary[i]
                top_pos = i
        return top_pos
