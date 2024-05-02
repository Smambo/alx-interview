#!/usr/bin/python3
"""Module for generating change"""


def makeChange(coins, total):
    """
    Function returns the fewest number of coins needed to make total
    Args:
      - coins(list[int]): list of values of coins available
      - total: amount needed
    """
    if total <= 0:
        return 0

    coin_count = 0
    coin_index = 0
    remainder = total
    sorted_coins = sorted(coins, reverse=True)
    num = len(coins)

    while remainder > 0:
        if coin_index >= num:
            return -1
        if remainder - sorted_coins[coin_index] >= 0:
            remainder -= sorted_coins[coin_index]
            coin_count += 1
        else:
            coin_index += 1
    return coin_count
