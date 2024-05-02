## Making Change
For this project, you will tackle a classic problem from the domain of dynamic programming and greedy algorithms: the coin change problem. The objective is to find the minimum number of coins required to make up a given total amount, given a list of coin denominations. This project challenges you to apply your understanding of algorithms to devise a solution that is not only correct but also efficient.

### Task:
[0. Change comes from within](./0-making_change.py)<br>
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount `total`.

* Prototype: `def makeChange(coins, total)`
* Return: fewest number of coins needed to meet `total`
  * If `total` is `0` or less, return `0`
  * If `total` cannot be met by any number of coins you have, return `-1`
* `coins` is a list of the values of the coins in your possession
* The value of a coin will always be an integer greater than `0`
* You can assume you have an infinite number of each denomination of coin in the list
* Your solution’s runtime will be evaluated in this task

```
simam@DESKTOP-5QTVNRV:~/alx-interview/0x08-making_change$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))
simam@DESKTOP-5QTVNRV:~/alx-interview/0x08-making_change$
simam@DESKTOP-5QTVNRV:~/alx-interview/0x08-making_change$ ./0-main.py
7
-1
simam@DESKTOP-5QTVNRV:~/alx-interview/0x08-making_change$
```
