#!/usr/bin/python3
"""
Below module calculates minimum number of operations needed
to result in `n` 'H' characters
"""


def minOperations(n):
    """
    Function calculates the minimun number of operations
    needed to result in n 'H' characters.
    Params:
        n(int): number of 'H' chars to be returned
    Returns:
        Mininum number of operations of n(int)
    """

    if not isinstance(n, int):
        return 0

    operations = 0
    clipboard = 0
    completed_op = 1

    while completed_op < n:
        if clipboard == 0:  # initialises the first copy & paste operation
            clipboard = completed_op
            completed_op += clipboard
            operations += 2
        elif n - completed_op > 0 and (n - completed_op) % completed_op == 0:
            clipboard = completed_op
            completed_op += clipboard
            operations += 2
        elif clipboard > 0:
            completed_op += clipboard
            operations += 1
    return (operations)
