#!/usr/bin/env python3
"""
The below module generates Pascal's Triangle
"""


def generate_next_row(row):
    """
    Generates subsequent row based on the current one
    Params:
        row(list): current row of the triangle
    Returns:
        list: next row of the triangle
    """
    next_row = [1]

    for i in range(1, len(row)):
        next_row.append(row[i - 1] + row[i])
    next_row.append(1)
    return (next_row)


def pascal_triangle(n):
    """
    Params:
        n(int): The number of rows to generate in the triangle
    Returns:
        list of integers representing
        the Pascal's triangle of n.
    """

    if n <= 0:
        return []

    triangle = [[1]]  # First row of the triangle

    for i in range(1, n):
        triangle.append(generate_next_row(triangle[-1]))

    return (triangle)


if __name__ == "__main__":
    pytest.main([__file__])
