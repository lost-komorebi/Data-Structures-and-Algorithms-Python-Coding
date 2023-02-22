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


def quick_sort1(li, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(li) - 1
    if left < right:  # if left smaller right, it means sublist contains at least two elements
        pivot_pos = partition(li, left, right)
        quick_sort1(li, left, pivot_pos-1)
        quick_sort1(li, pivot_pos+1, right)


def partition(li, left, right):
    """ calculate index of new pivot """
    l = left  # left_mark index
    r = right - 1  # right_mark index is the second last element
    pivot = li[right]  # set last element as pivot

    while l < r:
        # left mark move to right until find element greater than pivot
        while li[l] < pivot and l < right:
            l += 1
        # right mark move to left until find element smaller than pivot
        while li[r] >= pivot and r > left:
            r -= 1
        if l < r:
            li[l], li[r] = li[r], li[l]

    # right_mark moves to the left side of left_mark, i.e: r < l
    # swap element at left mark and pivot
    # l will be the index of new pivot
    if li[l] > pivot:
        li[l], li[right] = li[right], li[l]

    return l


if __name__ == '__main__':

    my_list = [9, 1, 6, 3, 4, 7, 2, 8, 0, 5]
    print(my_list)
    my_list = quick_sort(my_list)
    print(my_list)
    my_list = [9, 1, 6, 3, 4, 7, 2, 8, 0, 5]
    quick_sort1(my_list)
    print(my_list)
