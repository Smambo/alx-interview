#!/usr/bin/python3
"""Prime game module"""


def isWinner(x, nums):
    """
    Args:
    - x(int): number of rounds of the game
    - nums(array[int]): array of n
    Function returns name of player that won the most rounds
    Otherwise None if winner cannot be determined
    """
    if x < 1 or not nums:
        return None
    maria_wins, ben_wins = 0, 0

    n = max(nums)  # generate primes with a limit of max num in nums
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False

    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # filter number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        ben_wins += primes_count % 2 == 0
        maria_wins += primes_count % 2 == 1
    if maria_wins == ben_wins:
        return None
    elif maria_wins > ben_wins:
        return 'Maria'
    else:
        return 'Ben'
