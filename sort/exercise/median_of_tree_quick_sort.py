#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   median_of_tree_quick_sort.py
@Time    :   2023/02/24 11:53:44
@Author  :   komorebi 
'''
"""
1. choose leftmost, middle, and rightmost elements, sort them in ascending order in the list
2. set up l, r counters, ignore leftmost and rightmost elements
3. partition as usual
"""




import random
import time
def quick_sort(li, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(li) - 1
    if left < right:
        pivot_pos = partition(li, left, right)
        quick_sort(li, left, pivot_pos - 1)  # sort left side
        quick_sort(li, pivot_pos + 1, right)  # sort right side


def partition(li, left, right):
    median_of_three(li, left, right)
    median_pos = (left + right) // 2
    # after choosing median of three, li[left] is smaller than median of three, so we don't need to perform comparison on it
    l = left + 1
    # after choosing median of three, li[right] is bigger than median of three, so we don't need to perform comparison on it
    r = right - 1

    pivot = li[median_pos]  # set midian of three as pivot

    while l < r:
        while li[l] < pivot:  # l cursor keep looking for element larger than pivot
            l += 1
        while li[r] > pivot:  # r cursor keep looking for element smaller than pivot
            r -= 1
        if l < r:
            li[l], li[r] = li[r], li[l]

    if li[l] < pivot:
        li[l], li[median_pos] = li[median_pos], li[l]
    return l


def median_of_three(li, left, right):
    """
    choose leftmost, middle, rightmost element and put those three elements in ascending order in the list
    """
    middle = (left + right) // 2
    if li[left] > li[right]:
        li[left], li[right] = li[right], li[left]
    if li[left] > li[middle]:
        li[left], li[middle] = li[middle], li[left]
    if li[right] < li[middle]:
        li[right], li[middle] = li[middle], li[right]


if __name__ == '__main__':
    li = random.sample(range(1, 10000), 1000)
    time1 = time.time()
    quick_sort(li)
    time2 = time.time()
    assert li == sorted(li)
    print(time2 - time1)
