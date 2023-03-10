#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   max_heap.py
@Time    :   2023/03/10 19:56:42
@Author  :   komorebi 
'''

"""
Implement a binary heap as a max heap.
"""




import random
class MaxHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0  # length and index of the last element of heap_list

    def insert(self, value):
        self.heap_list.append(value)
        self.current_size += 1
        self.percolate_up(self.current_size)

    def percolate_up(self, index):
        while index // 2 > 0:
            if self.heap_list[index] > self.heap_list[index // 2]:
                self.heap_list[index], self.heap_list[index //
                                                      2] = self.heap_list[index // 2], self.heap_list[index]
            index = index // 2

    def percolate_down(self, index):
        while index * 2 <= self.current_size:  # current element has at least one child
            max_child_index = self.get_max_child_index(index)
            if self.heap_list[index] < self.heap_list[max_child_index]:
                self.heap_list[index], self.heap_list[max_child_index] = self.heap_list[max_child_index], self.heap_list[index]
            index = max_child_index

    def get_max_child_index(self, index):
        if index * 2 + 1 > self.current_size:  # only has left child
            return index * 2
        else:  # has both left and right child
            if self.heap_list[index * 2] > self.heap_list[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1

    def del_max(self):
        max_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.heap_list.pop()
        self.current_size -= 1
        self.percolate_down(1)
        return max_value

    def build_heap(self, new_list):
        self.heap_list = [0] + new_list
        self.current_size = len(new_list)
        idx = self.current_size // 2
        while idx > 0:
            self.percolate_down(idx)
            idx -= 1


if __name__ == '__main__':
    max_heap = MaxHeap()
    ll = [2, 7, 26, 25, 19, 17, 1, 90, 3, 36]
    # random.shuffle(ll)
    # print(ll)
    # print(max_heap.build_heap(ll))
    for i in ll:
        max_heap.insert(i)
    print(max_heap.heap_list)
    max_heap.del_max()
    print(max_heap.heap_list)
    max_heap.del_max()
    print(max_heap.heap_list)
