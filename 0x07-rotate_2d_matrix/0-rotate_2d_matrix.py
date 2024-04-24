#!/usr/bin/python3
"""Module for a 2D matrix rotation"""


def rotate_2d_matrix(matrix):
    """Function does an inplace rotation of a
    2D matrix 90 degrees clockwise
    """
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return

    m = len(matrix)  # values on horizontal axis (row)
    n = len(matrix[0])  # values on vertical axis (col)

    if not all(map(lambda x: len(x) == n, matrix)):
        return

    col, row = 0, m - 1
    for i in range(n * m):
        if i % m == 0:
            matrix.append([])
        if row == -1:
            row = m - 1
            col += 1
        matrix[-1].append(matrix[row][col])

        if col == n - 1 and row >= -1:
            matrix.pop(row)
        row -= 1
