#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
time complexity: O(N^2)
space complexity: O(1)
no need extra space
"""


def bubble_sort(li: list):
    for i in range(len(li) - 1):
        for j in range(len(li) - 1 - i):
            if li[j] > li[j + 1]:  # compare with next element repeatedly
                li[j], li[j + 1] = li[j + 1], li[j]  # swap location


if __name__ == '__main__':
    my_list = [9, 1, 6, 3, 4, 7, 2, 8, 0, 5]
    bubble_sort(my_list)
    print(my_list)
