#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   binary_insertion_sort.py
@Time    :   2023/04/30 23:12:29
@Author  :   komorebi 
'''
"""
Even though this algorithm uses binary search, 
it is usually slower than the original insertion sort 
because the original insertion sort combines the search and insertion processes, 
whereas binary insertion sort separates them. 
This separation increases the time required, 
which is why it takes more time than the original insertion sort.
"""


def binary_insertion_sort(li):
    n = len(li)
    for i in range(1, n):
        val = li[i]
        j = binary_search(li, 0, i-1, val)
        while i > j:  # move those elements which are bigger than val right
            li[i] = li[i-1]
            i -= 1
        li[i] = val  # insert val at the proper index


def binary_search(li, start, end, val):
    """ Return the index at which the new element should be inserted """
    if start == end:  # the list only has one list or we have the last element to compare with the new element
        if li[start] > val:
            return start
        else:
            return start + 1
    if start > end:  # new element is smaller than all the elements in the sorted area of the list
        return start
    mid = (start + end) // 2
    if val > li[mid]:
        return binary_search(li, mid+1, end, val)
    elif val < li[mid]:
        return binary_search(li, 0, mid-1, val)
    else:
        return mid


if __name__ == '__main__':
    li = [15, 87, 4, 111, 43, 56, 3, 222, 48, 87, 11]
    binary_insertion_sort(li)
    print(li)
    assert li == sorted(li)
