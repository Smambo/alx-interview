#!/usr/bin/python3
"""Module for a 2D matrix rotation"""


def rotate_2d_matrix(matrix):
    """Function does an inplace rotation of a
    2D matrix 90 degrees clockwise
    """
    if not isinstance(matrix, list):
        return
    if not matrix or not all(isinstance(row, list) for row in matrix):
        return

    m = len(matrix)  # values on horizontal axis (row)
    n = len(matrix[0])  # values on vertical axis (col)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse the rows
    for i in range(m):
        matrix[i].reverse()
