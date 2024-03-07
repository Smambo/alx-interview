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
    
    triangle_output = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle_output[i - 1]
        
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle_output.append(row)
    return (triangle_output)


if __name__ == "__main__":
    pytest.main([__file__])
