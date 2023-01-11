#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
time complexity: O(NlogN)
space complexity: O(N)
"""

import random


def quick_sort(li: list):
    if len(li) <= 1:
        return li
    else:
        pivot = li.pop()
        left, right = [], []
        for i in li:
            if i > pivot:
                right.append(i)
            else:
                left.append(i)
    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == '__main__':
    my_list = [random.randint(0, 100) for _ in range(10)]
    print(my_list)
    my_list = quick_sort(my_list)
    print(my_list)
