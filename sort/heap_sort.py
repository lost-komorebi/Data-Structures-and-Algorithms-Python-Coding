#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
step 1: insert data to binary heap tree
step 2: extract data from binary heap tree
"""


def heapify(li: list, n: int, index: int):
    """
    :param li: list to sort
    :param n: the number of elements should heapify in the list
    :param index: index of list to sort
    :return:
    """
    max_index = index  # assume li[index] is the largest
    l = 2 * index + 1  # left index, index starts from 0
    r = 2 * index + 2  # right index
    if l < n and li[max_index] < li[l]:
        max_index = l
    if r < n and li[max_index] < li[r]:
        max_index = r
    if max_index != index:  # swap largest value and current value
        li[index], li[max_index] = li[max_index], li[index]
        heapify(li, n, max_index)


def heap_sort(li: list):
    n = len(li)
    # we start from last parent(n//2-1) to the root
    # step 1, perform a binary heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(li, n, i)

    # step 2, swap root and last(li[n-1]), so the last element is the biggest
    # then heapify the heap, swap li[n-2] and root, so from li[n-2] to last are sorted
    # keep doing like, until all elements are sorted
    for i in range(n - 1, 0, -1):
        li[0], li[i] = li[i], li[0]
        heapify(li, i, 0)


my_list = [0, 2, 1, 5, 4, 6, 9, 8, 7, 3]
heap_sort(my_list)
print(my_list)
