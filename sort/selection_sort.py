#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
suitable for small list
no need extra space
time complexity: O(N^2)
space complexity: O(1)
"""


def selection_sort(li: list):
    # for n numbers, we just need to loop n - 1 times, we can get the list ordered
    for i in range(len(li) - 1):
        min_index = i  # we assume the first number in the unsorted area is the smallest
        # find the minimum value from the unsorted area
        # we don't need to compare i vs i, so we start from i + 1
        for j in range(i+1, len(li)):
            if li[min_index] > li[j]:
                min_index = j
        # put minimum value at the sorted area
        # index < i belong to sorted area
        li[i], li[min_index] = li[min_index], li[i]


if __name__ == '__main__':
    my_list = [9, 1, 6, 3, 4, 7, 2, 8, 0, 5]
    selection_sort(my_list)
    print(my_list)
