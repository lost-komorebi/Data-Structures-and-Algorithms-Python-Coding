#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   heap_sort.py
@Time    :   2023/03/11 19:21:09
@Author  :   komorebi 
'''

"""
Using the buildHeap method, write a sorting function that can sort a list in O(nlogn)time.
"""




import random
from min_heap import MinHeap
def heap_sort(li: list):
    min_heap = MinHeap()
    min_heap.build_heap(li)  # O(n) time complexity
    n = len(li)
    i = 0
    # while iteration O(n) time complexity is O(nlogn) time complexity
    # del_min() is O(logn) time complexity
    # so code below is O(nlogn) time complexity
    while i < n:
        li[i] = min_heap.del_min()
        i += 1


if __name__ == '__main__':
    ll = [2, 7, 26, 25, 19, 17, 1, 90, 3, 36]
    random.shuffle(ll)
    print(ll)
    print(heap_sort(ll))
    print(ll)
