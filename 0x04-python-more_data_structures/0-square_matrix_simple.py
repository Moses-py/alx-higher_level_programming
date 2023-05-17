#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    store_matrix_arr = []
    for column in matrix:
        sol = list(map(lambda x: x**2, column))
        store_matrix_arr.append(sol)
    return store_matrix_arr
