#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
import time
"""
Problem Statement:
Given N, find the number of ways to express N as a sum of 1, 3 and 4.
Example 1
-N=4
- Number of ways = 4
- Explanation : There are 4 ways we can express N. {4},{1,3},{3,1},{1,1,1,1}
"""


def number_factor(n):
    """ we just need to return the number of combinations """
    if n == 0:
        return
    elif n in (1, 2):
        return 1  # n = 1,  {1} ; n = 2 {1, 1}
    elif n == 3:
        return 2  # {1, 2} {2, 1}
    elif n == 4:  # {1, 1, 1, 1} {1, 3} {3, 1} {4}
        return 4
    else:
        sub1 = number_factor(n - 1)
        sub2 = number_factor(n - 3)
        sub3 = number_factor(n - 4)
        return sub1 + sub2 + sub3


def number_factor_tabulation(n):
    """ dynamic programming approach """
    tabulation = [0, 1, 1, 2, 4]
    for i in range(5, n+1):
        tabulation.append(tabulation[i - 1] +
                          tabulation[i - 3] + tabulation[i - 4])
    return tabulation[n]


def number_factor_memoization(n, memoization={}):
    """ we just need to return the number of combinations """
    if n == 0:
        return
    elif n in (1, 2):
        return 1  # n = 1,  {1} ; n = 2 {1, 1}
    elif n == 3:
        return 2  # {1, 2} {2, 1}
    elif n == 4:  # {1, 1, 1, 1} {1, 3} {3, 1} {4}
        return 4
    else:
        if n not in memoization:
            memoization[n] = number_factor_memoization(n - 1, memoization) + number_factor_memoization(
                n - 3, memoization) + number_factor_memoization(n - 4, memoization)
    return memoization[n]


if __name__ == '__main__':
    n = 40
    time1 = time.time()
    print(number_factor(n))
    time2 = time.time()
    print(time2 - time1)
    print(number_factor_tabulation(n))
    time3 = time.time()
    print(time3 - time2)
    print(number_factor_memoization(n))
    time4 = time.time()
    print(time4 - time1)
