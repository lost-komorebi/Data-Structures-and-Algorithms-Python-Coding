#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
time complexity: O(NlogN)
space complexity: O(N)
"""

import random


def merge_sort(li: list):
    if len(li) > 1:
        left = li[:len(li) // 2]
        right = li[len(li) // 2:]

        # recursion
        merge_sort(left)
        merge_sort(right)

        i = 0  # left index
        j = 0  # right index
        k = 0  # merged list index

        # merge left and right
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                li[k] = left[i]
                i += 1
                k += 1
            else:
                li[k] = right[j]
                j += 1
                k += 1

        # check if any element was left
        while i < len(left):
            li[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            li[k] = right[j]
            j += 1
            k += 1


if __name__ == '__main__':
    random.seed('list')
    my_list = [random.randint(0, 10) for _ in range(10)]
    print(my_list)
    merge_sort(my_list)
    print(my_list)
