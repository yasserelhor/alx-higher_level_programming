#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrixa = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    for r in range(3):
        for c in range(3):
            matrixa[r][c] = matrix[r][c] ** 2

    return matrixa


