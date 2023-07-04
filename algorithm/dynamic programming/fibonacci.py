#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
Definition : a series of numbers in which each number is the sum of the two preceding numbers. 
First two numbers by definition are 0 and 1.
Example : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ....
"""


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memoization(n, memo: dict):
    """ Top-down approach by using memoization """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if n not in memo:
        memo[n] = fibonacci_memoization(
            n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]


def fibonacci_tabulation(n):
    """ Bottom-up approach by using tabulation """
    tb = [0, 1]
    for i in range(2, n+1):
        tb.append(tb[i-1] + tb[i-2])
    return tb[n]


if __name__ == '__main__':
    n = 25
    print(fibonacci(n))
    print(fibonacci_memoization(n, {}))
    print(fibonacci_tabulation(n))
