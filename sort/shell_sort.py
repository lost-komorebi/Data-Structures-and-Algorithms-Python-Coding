#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   shell_sort.py
@Time    :   2023/02/21 17:03:45
@Author  :   komorebi 
'''
"""
The method starts by sorting pairs of elements far apart from each other, 
then progressively reducing the gap between elements to be compared. 
By starting with far apart elements, 
it can move some out-of-place elements into position faster 
than a simple nearest neighbor exchange
"""


def shell_sort1(li):
    gap = len(li) // 2  # init gap
    while gap > 0:
        # insertion sort
        for i in range(gap, len(li)):
            current_value = li[i]
            position = i
            while position > 0 and li[position-1] > current_value:
                li[position] = li[position-1]
                position -= 1
            li[position] = current_value
        gap = gap // 2  # reduce gap


def shell_sort2(li):
    gap = len(li) // 2  # init gap
    while gap > 0:
        for start_index in range(gap):
            # set gap as step, thus reducing element swaps
            gap_insert_sort(start_index, gap, li)
        gap = gap // 2  # reduce gap


def gap_insert_sort(start, gap, li):
    """ 
    use a gap here as step to perform insertion sort, 
    so we reduce element swaps compare to shell_sort1 in current file
    """
    for i in range(start+gap, len(li), gap):
        current_value = li[i]
        position = i
        while position >= gap and li[position-gap] > current_value:
            li[position] = li[position-gap]
            position -= gap
        li[position] = current_value


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shell_sort1(li)
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shell_sort2(li)
    print(li)
