#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   quick_insertion_hybrid.py
@Time    :   2023/02/27 21:02:23
@Author  :   komorebi 
'''

"""
One way to improve the quick sort is to use an insertion sort on lists 
that have a small length (call it the “partition limit”). 
Re-implement the quick sort and use it to sort a random list of integers.
"""

"""
set a threshold value, if the size is greater than threshold value, 
then quick sort will perform on that partion of array,
else insertion sort will perform
"""




import random
import time
def insertion_sort(li: list, left, right):
    for i in range(left, right+1):
        current_value = li[i]
        position = i
        while position > 0 and li[position-1] > current_value:
            li[position] = li[position-1]
            position -= 1
        li[position] = current_value


def quick_sort(li: list, left: int = 0, right: int = None) -> None:
    if right is None:
        right = len(li) - 1
    if left < right:
        pivot_pos = partition(li, left, right)
        quick_sort(li, left, pivot_pos - 1)
        quick_sort(li, pivot_pos + 1, right)


def partition(li, left, right):
    l = left
    r = right - 1
    pivot = li[right]

    while l < r:
        while li[l] < pivot and l < right:
            l += 1
        while li[r] > pivot and r > left:
            r -= 1
        if l < r:
            li[l], li[r] = li[r], li[l]

    if li[l] > pivot:
        li[l], li[right] = li[right], li[l]

    return l


def hybrid(li: list, left: int = 0, right: int = None) -> None:
    if right is None:
        right = len(li) - 1
    if right - left + 1 < 10:  # length < thredhold, insertion sort
        insertion_sort(li, left, right)
    else:
        if left < right:  # quick sort
            pivot_pos = partition(li, left, right)
            hybrid(li, left, pivot_pos - 1)
            hybrid(li, pivot_pos + 1, right)


if __name__ == '__main__':
    li = list(range(100))
    hybrid(li)
    print(li)
