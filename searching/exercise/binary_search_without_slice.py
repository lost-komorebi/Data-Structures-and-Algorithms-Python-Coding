#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   binary_search.py
@Time    :   2023/02/25 12:18:33
@Author  :   komorebi 
'''

"""
Implement the binary search using recursion without the slice operator.
Recall that you will need to pass the list along with the starting and ending index values 
for the sublist.
"""




import random
def recursive_binary_search(li: list, n: int, start: int = 0, end: int = None) -> bool:
    if end is None:
        end = len(li) - 1  # index of last element
    if start > end:
        return False
    midpoint = (start + end) // 2
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
    li = list(range(100))
    for i in range(-100, 100):
        if (i in li) != iterative_binary_search(li, i):
            print(i, (i in li), iterative_binary_search(li, i))
        if (i in li) != recursive_binary_search(li, i):
            print(i, (i in li), recursive_binary_search(li, i))

    
