#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
You are given coins of different denominations and total amount of money. Find the minimum number of coins that you need yo make up the given amount.
Infinite supply of denominations : {1,2,5,10,20,50,100,1000}
"""


def get_change(coins, change):
    coins = sorted(coins, reverse=True)
    result = []
    while change > 0:
        for i in coins:
            if i <= change:
                result.append(i)
                break
        change -= i
    return len(result)


if __name__ == '__main__':
    coins = {1, 2, 5, 10, 20, 50, 100, 1000}
    change = 2038
    get_change(coins, change)
