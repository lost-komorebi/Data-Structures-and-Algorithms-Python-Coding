#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
time complexity: O(N^2)
space complexity: O(1)
"""


def insertion_sort(li: list):
    for i in range(1, len(li)):
        j = i
        # compare element with elements which are in sorted area
        while li[j - 1] > li[j] and j > 0:
            li[j - 1], li[j] = li[j], li[j - 1]  # swap location
            j -= 1


if __name__ == '__main__':
    my_list = [9, 1, 6, 3, 4, 7, 2, 8, 0, 5]
    print(my_list)
    insertion_sort(my_list)
    print(my_list)
