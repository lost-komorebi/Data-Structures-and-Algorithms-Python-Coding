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


def insertion_sort1(li):
    for i in range(1, len(li)):
        # current value is the first element in unordered area
        current_value = li[i]
        position = i
        # compare the last element in ordered area with current_value
        # if it larger than current_value, then move it to current_value's location
        # continue compare the second last element in ordered area with current_value
        # and keep doing same operations
        while position > 0 and li[position-1] > current_value:
            li[position] = li[position-1]
            position -= 1
        # now the element at position index is smaller than current_value
        # so we insert current_value at position location
        li[position] = current_value


if __name__ == '__main__':
    my_list = [9, 1, 6, 3, 4, 7, 2, 8, 0, 5]
    print(my_list)
    insertion_sort(my_list)
    print(my_list)
    my_list = [9, 1, 6, 3, 4, 7, 2, 8, 0, 5]
    insertion_sort1(my_list)
    print(my_list)
