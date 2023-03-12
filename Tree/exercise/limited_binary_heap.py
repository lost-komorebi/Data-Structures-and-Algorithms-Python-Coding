#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   limited_binary_heap.py
@Time    :   2023/03/12 10:21:56
@Author  :   komorebi 
'''

"""
Create a binary heap with a limited heap size. 
In other words, the heap only keeps track of the n most important items. 
If the heap grows in size to more than n items the least important item is dropped.
"""




from min_heap import MinHeap
class LimitedBinaryHeap(MinHeap):
    def __init__(self, max_size):
        self.max_size = max_size
        super().__init__()

    def insert(self, value):
        if self.current_size < self.max_size:
            return super().insert(value)
        else:
            self.del_min()
            return super().insert(value)


if __name__ == '__main__':
    min_heap = LimitedBinaryHeap(5)
    ll = [2, 7, 26, 25, 19]
    print(min_heap.build_heap(ll))
    min_heap.insert(1)
    print(min_heap.heap_list)
    min_heap.insert(8)
    print(min_heap.heap_list)
