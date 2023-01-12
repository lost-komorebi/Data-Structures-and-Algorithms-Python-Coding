#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
only suitable for sorted array
time complexity: O(logN)
space complexity: O(1)
"""
import random
import math


def binary_search(li: list, n):
    """ divide list into two part, until find the specific value """
    left = li[:len(li) // 2]
    right = li[len(li) // 2:]
    while len(left) > 0 and len(right) > 0:
        if left[-1] == n:
            return left[-1]
        elif right[0] == n:
            return right[0]
        if left[-1] > n:
            right = left[len(left) // 2:]  # right first
            left = left[:len(left) // 2]
        elif left[-1] < n:
            left = right[:len(right) // 2]
            right = right[len(right) // 2:]
    return None


def binary_search1(li: list, n):
    """ define two cursors, move cursors until find the specific value """
    start = 0  # start index
    end = len(li) - 1  # end index
    middle = (start + end) // 2
    while not li[middle] == n and start <= end:
        if li[middle] > n:
            end = middle - 1  # move end to the left of middle
        else:
            start = middle + 1  # move start to the right of middle
        middle = (start + end) // 2
    if li[middle] == n:
        return li[middle]
    return None


if __name__ == '__main__':
    # my_list = sorted([random.randint(1, 10000) for _ in range(10000)])
    my_list = sorted([random.uniform(0, 1) for _ in range(10000)])
    # my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search1(my_list, random.choice(my_list)))
