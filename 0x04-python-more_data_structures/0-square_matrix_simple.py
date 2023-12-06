#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrixa = []

    for r in matrix:
        res = list(map(lambda x: x ** 2, r))
        matrixa.append(res)
    return matrixa
