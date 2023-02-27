#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   merge_sort_without_slice.py
@Time    :   2023/02/27 14:40:22
@Author  :   komorebi 
'''

"""
Implement the merge_sort function without using the slice operator
"""




import random
def merge_sort(li: list, start: int=0, end: int=None) -> None:

    if end is None:
        end = len(li)
    if end - start > 1:
        mid = (start + end) // 2

        merge_sort(li, start, mid)
        merge_sort(li, mid, end)

        i, j = start, mid

        result = []

        while i < mid and j < end:
            if li[i] < li[j]:
                result.append(li[i])
                i += 1
            else:
                result.append(li[j])
                j += 1

        while i < mid:
            result.append(li[i])
            i += 1

        while j < end:
            result.append(li[j])
            j += 1
        li[start:end] = result


if __name__ == '__main__':
    li = [5, 3, 6, 1, 8, 0, 7, 9, 4, 2]
    random.shuffle(li)
    print(li)
    merge_sort(li)
    print(li)
