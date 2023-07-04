#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
Problem Statement:
- Given N number of houses along the street with some amount of money - Adjacent houses cannot be stolen
- Find the maximum amount that can be stolen
Example:
[6, 7, 1, 30, 8, 2, 4]
Answer
- Maximum amount = 41
- Houses that are stolen : 7, 30, 4
"""


def house_robber(houses):
    """
    this approach is very slow
    option 1: rob the first house and then start from the third house
    option 2: rob start from the second house
    """
    if not houses:
        return
    if len(houses) == 1:
        return houses[0]
    if len(houses) == 2:
        return max(houses)
    return max(houses[0] + house_robber(houses[2:]), house_robber(houses[1:]))


def house_robber_tabulation(houses):
    """
    dynamic Bottom-up approach
    """
    if not houses:
        return
    # only 1 element
    if len(houses) == 1:
        return houses[0]
    # memoize first two results
    tabulation = [-1 for i in range(len(houses))]
    tabulation[0] = houses[0]
    tabulation[1] = max(houses[:2])
    # complete calculation all houses
    for i in range(2, len(houses)):
        tabulation[i] = max(houses[i] + tabulation[i - 2], tabulation[i - 1])
    return tabulation[len(houses) - 1]


def house_robber_memoization(houses):
    """
    dynamic Top-down approach
    """
    if not houses:
        return
    # less than 3 elements, return maximum
    if len(houses) <= 2:
        return max(houses)
    memoization = [-1 for i in range(len(houses))]

    def helper(i):
        if i < 0: # i < 0 we have calculated all houses
            return 0
        elif memoization[i] >= 0: # current i has already calculated
            return memoization[i]
        else: # wait for calculation
            memoization[i] = max(houses[i] + helper(i - 2), helper(i - 1))
            return memoization[i]
    return helper(len(houses) - 1)


if __name__ == '__main__':
    houses = [183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238,
              168, 128, 177, 235, 50, 81, 185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]
    print(house_robber_tabulation(houses))
    print(house_robber_memoization(houses))
    print(house_robber(houses))
