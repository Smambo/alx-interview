#!/usr/bin/env python3


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
    elif n == 1:
        return [[1]]
    else:
        prev_triangle = pascal_triangle(n - 1)
        row_end = prev_triangle[-1]
        new_row = [1]

        for i in range(1, len(row_end)):
            new_row.append(row_end[i - 1] + row_end[i])
        new_row.append(1)

        return (prev_triangle + [new_row])


if __name__ == "__main__":
    pytest.main([__file__])
