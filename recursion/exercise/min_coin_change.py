#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   min_coin_change.py
@Time    :   2023/02/15 15:41:16
@Author  :   komorebi 
'''

""" get the minimua number of coins for specific number """

import time
coins = [25, 10, 5, 1]


def get_min_coins1(n):
    """ use while loop """
    min_coins = 0
    while n > 0:
        for i in coins:
            if n >= i:
                min_coins += 1
                n -= i
                break
    return min_coins


def get_min_coins2(n):
    """ use recursion """
    min_coins = n
    if n in coins:  # n in coins, we just need 1 coin
        return 1
    else:
        for i in [c for c in coins if c < n]:
            num_coins = 1 + get_min_coins2(n - i)
            min_coins = min(num_coins, min_coins)
        return min_coins


def get_min_coins3(n, known_result=None):
    """ store calculated results, avoid dupicate calculations """
    min_coins = n
    if not known_result:
        known_result = [0 for i in range(n+1)]
    if n in coins:  # n in coins, we just need 1 coin
        known_result[n] = 1
        return 1
    elif known_result[n] > 0:
        return known_result[n]
    else:
        for i in [c for c in coins if c < n]:
            num_coins = 1 + get_min_coins3(n - i, known_result)
            min_coins = min(num_coins, min_coins)
            known_result[n] = min_coins
        return min_coins


if __name__ == '__main__':
    time1 = time.time()
    print(get_min_coins1(63))
    time2 = time.time()
    print(time2 - time1)
    time3 = time.time()
    print(get_min_coins2(63))
    time4 = time.time()
    print(time4 - time3)
    time5 = time.time()
    print(get_min_coins3(63))
    time6 = time.time()
    print(time6 - time5)
