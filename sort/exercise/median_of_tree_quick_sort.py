#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   median_of_tree_quick_sort.py
@Time    :   2023/02/24 11:53:44
@Author  :   komorebi 
'''
"""
median of three: To choose the pivot value, we will consider the first, 
the middle, and the last element in the list. In our example, those are 54, 77, and 20.
Now pick the median value, in our case 54, and use it for the pivot value.
Devise alternative strategies for choosing the pivot value in quick sort. 
For example, pick the middle item. 
Re-implement the algorithm and then execute it on random data sets. 
Under what criteria does your new strategy perform better or worse than the strategy from this chapter.
conclusion: if the mid number is the median of three, then this algorithm performs better
"""




import random
import time
def quick_sort1(li: list, left: int = None, right: int = None) -> None:
    """ use last element as pivot """
    if left is None:
        left = 0
    if right is None:
        right = len(li) - 1
    if left < right:
        pivot_pos = partition1(li, left, right)
        quick_sort1(li, left, pivot_pos-1)
        quick_sort1(li, pivot_pos+1, right)


def partition1(li: list, left: int, right: int) -> int:
    l = left
    r = right-1
    pivot = li[right]

    while l < r:
        while l < right and li[l] < pivot:
            l += 1
        while r > left and li[r] >= pivot:
            r -= 1

        if l < r:
            li[l], li[r] = li[r], li[l]

    if li[l] > pivot:
        li[l], li[right] = li[right], li[l]
    return l


def quick_sort2(li: list, left: int = None, right: int = None) -> None:
    """ use first element as pivot """
    if left is None:
        left = 1
    if right is None:
        right = len(li) - 1
    if left < right:
        pivot_pos = partition2(li, left, right)
        quick_sort2(li, left, pivot_pos-1)
        quick_sort2(li, pivot_pos+1, right)


def partition2(li: list, left: int, right: int) -> int:
    l = left
    r = right
    pivot = li[left]
    while l < r:
        while l < right and li[l] < pivot:
            l += 1
        while r > left and li[r] >= pivot:
            r -= 1

        if l < r:
            li[l], li[r] = li[r], li[l]

    if li[r] < pivot:
        li[r], li[left] = li[left], li[r]

    return r


def quick_sort3(li: list, left: int = None, right: int = None) -> None:
    """ use mid element as pivot """
    if left is None:
        left = 0
    if right is None:
        right = len(li) - 1
    if left > 1 and right > 1:
        pivot_pos = partition3(li, left, right)
        quick_sort3(li, left, pivot_pos-1)
        quick_sort3(li, pivot_pos+1, right)


def partition3(li: list, left: int, right: int) -> int:
    l = left
    r = right
    mid = len(li)//2
    pivot = li[mid]

    while l < r:
        while l < right and li[l] < pivot:
            l += 1
        while r > right and li[r] > pivot:
            r -= 1

        if li[l] > li[r]:
            li[l], li[r] = li[r], li[l]

    if li[l] > pivot:
        li[l], li[mid] = li[mid], li[l]
    return l


def median_of_tree(li: list) -> int:
    temp = [li[0], li[-1], li[len(li)//2]]
    return list(set(temp) - set([min(temp), max(temp)]))[0]


def quick_sort(li):
    median = median_of_tree(li)
    if median == li[0]:
        quick_sort1(li)
    elif median == li[-1]:
        quick_sort2(li)
    else:
        quick_sort3(li)


if __name__ == '__main__':
    li = [random.randint(0, 1000000) for _ in range(1000000)]
    print(median_of_tree(li), [li[0], li[len(li)//2], li[-1]])
    time1 = time.time()
    quick_sort(li)
    time2 = time.time()
    print(time2 - time1)
