#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   binary_search.py
@Time    :   2023/02/25 12:18:33
@Author  :   komorebi 
'''

"""
Implement the binary search using recursion without the slice operator.
 Recall that you will need to pass the list along with the starting and ending index values for the sublist.
"""




import random
def recursive_binary_search(li: list, n: int, start: int = None, end: int = None) -> bool:
    if start is None:
        start = 0  # index of first element
    if end is None:
        end = len(li) - 1  # index of last element
    if start >= end:
        return False
    length = end - start + 1
    midpoint = length // 2
    print(start, end, length, midpoint, li[start:end])
    if n == li[midpoint]:
        return True
    elif n < li[midpoint]:
        return recursive_binary_search(li, n, start, midpoint-1)
    else:
        return recursive_binary_search(li, n, midpoint+1, end)


def iterative_binary_search(li: list, n: int) -> bool:
    start = 0
    end = len(li) - 1
    while start <= end:
        midpoint = (start + end) // 2
        if n == li[midpoint]:
            return True
        elif n < li[midpoint]:
            end = midpoint - 1
        else:
            start = midpoint + 1
    return False


if __name__ == '__main__':
    li = list(range(99))
    #print(recursive_binary_search(li, 0))
    for i in range(-100, 100):
        if (i in li) != iterative_binary_search(li, i):
            print(i, (i in li), iterative_binary_search(li, i))
    #     if (i in li) != recursive_binary_search(li, i):
    #         print(i, (i in li), recursive_binary_search(li, 0))

    #print(recursive_binary_search(li, 100))
