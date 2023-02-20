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


def short_bubble_sort(li: list):
    """ 
    we loop through the list len(li) - 1 times, 
    if during a loop, we couldn't find any elements to swap
    it means the list is ordered, so we stop the loop
    """
    for pass_num in range(len(li) - 1, 0, -1):
        need_swap = False  # assume li is ordered
        for i in range(pass_num):
            if li[i] > li[i+1]:
                need_swap = True  # if we found any unordered part, we still need to swap
                li[i], li[i+1] = li[i+1], li[i]
        if need_swap == False:  # no swap need to do, current li is ordered
            break


if __name__ == '__main__':
    my_list = [9, 1, 6, 3, 4, 7, 2, 8, 0, 5]
    bubble_sort(my_list)
    print(my_list)
    my_list1 = [44, 20, 17, 26, 31, 54, 55, 77, 93]
    short_bubble_sort(my_list1)
    print(my_list1)
