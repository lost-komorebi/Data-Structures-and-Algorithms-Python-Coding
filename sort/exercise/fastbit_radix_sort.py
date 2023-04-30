#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   fastbit_radix_sort.py
@Time    :   2023/04/30 23:18:32
@Author  :   komorebi 
'''
"""
reference: https://ieeexplore.ieee.org/document/7822019
"""




import random
import time
def sort_binary_data(li):
    n = len(li)
    start = 0
    end = n - 1

    while start < end:
        if li[start] < li[end]:
            start += 1
            end -= 1
        elif li[start] > li[end]:
            li[start], li[end] = li[end], li[start]
            start += 1
            end -= 1
        else:  # if they are euqal
            if li[start] == 0:
                start += 1
            else:
                end -= 1


def fastbit_radix_sort(li, lb=0, ub=None, bitposition=None):
    # print(lb, ub, bitposition)
    if ub is None:
        ub = len(li) - 1
    if bitposition is None:
        bitposition = 1 << 31

    if ub <= lb or bitposition == 0:
        # print(bitposition)
        return

    start = lb
    end = ub

    while start <= end:
        if (li[start] & bitposition) < (li[end] & bitposition):
            start += 1
            end -= 1
        elif (li[start] & bitposition) > (li[end] & bitposition):
            li[start], li[end] = li[end], li[start]
            start += 1
            end -= 1
        else:  # they are equal
            if (li[start] & bitposition) == 0:
                start += 1
            else:
                end -= 1

    fastbit_radix_sort(li, lb, start - 1, bitposition >> 1)
    fastbit_radix_sort(li, start, ub, bitposition >> 1)


def fastbit_radix_sort_optimized(li: list, lb: int = 0, ub: int = None, bit=None):
    """
    lb: lowerband means the start index of the list
    ub: upbound means the end index of the list
    """
    if ub is None:
        ub = len(li) - 1
    if bit is None:  # calulate bit
        bit = 2 ** (max(li).bit_length() - 1)
    # there is only one element or less, all elements are sorted
    if ub <= lb or bit == 0:
        return

    start = lb
    end = ub

    while start <= end:
        if (li[start] & bit) < (li[end] & bit):
            start += 1
            end -= 1
        elif (li[start] & bit) > (li[end] & bit):
            li[start], li[end] = li[end], li[start]
            start += 1
            end -= 1
        else:  # they are equal
            if (li[start] & bit) == 0:
                start += 1
            else:
                end -= 1

    # 0's partition
    if (start-1) - lb == 1:  # only two elements in 0's partition
        if li[lb] > li[start - 1]:
            li[lb], li[start - 1] = li[start - 1], li[lb]
    else:  # more than two elements in 0's partition
        fastbit_radix_sort_optimized(li, lb, start - 1, bit >> 1)

    # 1's partition
    if (ub-start) == 1:  # only two elements in 1's partition
        if li[start] > li[ub]:
            li[start], li[ub] = li[ub], li[start]
    else:  # more than two elements in 1's partition
        fastbit_radix_sort_optimized(li, start, ub, bit >> 1)


if __name__ == '__main__':

    binary_list = [0, 1, 0, 1, 0, 1, 1]
    print(binary_list)
    sort_binary_data(binary_list)
    print(binary_list)

    li = [random.randint(0, 100) for _ in range(10)]
    print(li)
    time1 = time.time()
    fastbit_radix_sort_optimized(li)
    time2 = time.time()
    print(time2 - time1)
    print(li)
    assert li == sorted(li)
