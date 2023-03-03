#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   min_heap.py
@Time    :   2023/03/02 10:06:14
@Author  :   komorebi 
'''

"""
using python list to implement a min binary heap
"""




import random
class MinHeap:
    def __init__(self):
        # heap start from index 1, 2x is left child, 2x+1 is right child
        self.heap_list = [0]
        self.current_size = 0  # record the length of heap

    def insert(self, value):
        """ 
        insert a new item to heap
        !!!if we use insert to loop from a list to perform a heap, the time complixity is O(NlogN)!!!
        """
        self.heap_list.append(value)
        self.current_size += 1
        self.percolate_up(self.current_size)

    def percolate_up(self, index):
        """
        percolate the newly added item up to its proper position in this tree
        """
        parent_index = index // 2
        while parent_index > 0:
            # compare newly added item with its parent
            if self.heap_list[index] < self.heap_list[parent_index]:
                # swap item with its parent because item smaller than its parent
                self.heap_list[index], self.heap_list[parent_index] = self.heap_list[parent_index], self.heap_list[index]
            index = parent_index
            parent_index = index // 2

    def percolate_down(self, index):
        """
        percolate the new root item down to its proper position in this tree
        """
        while index * 2 <= self.current_size:  # if current item has no child, while will not continue
            min_child_index = self.get_min_child_index(index)
            if self.heap_list[index] > self.heap_list[min_child_index]:
                # swap item with its parent because item greater than its parent
                self.heap_list[index], self.heap_list[min_child_index] = self.heap_list[min_child_index], self.heap_list[index]
            index = min_child_index

    def get_min_child_index(self, index):
        """
        returen the index of its smallest child 
        """
        if index * 2 + 1 > self.current_size:  # current item has no right child
            return index * 2
        else:  # compare left and right child and return the index of the smaller one
            if self.heap_list[index * 2] > self.heap_list[index * 2 + 1]:
                return index * 2 + 1
            else:
                return index * 2

    def del_min(self):
        """ delete minimal value from heap list"""
        min_value = self.heap_list[1]
        # move the last item to the root postion
        self.heap_list[1] = self.heap_list[self.current_size]
        self.heap_list.pop()  # pop last item
        self.current_size -= 1
        self.percolate_down(1)
        return min_value

    def build_heap(self, new_list):
        """ 
        time complexity : O(N) 
        the result of this function may show differences with loop through a list and use insert function to perfrom heap
        """
        i = len(new_list) // 2
        self.current_size = len(new_list)
        self.heap_list = [0] + new_list[:]
        while i > 0:  # maintain heap property
            self.percolate_down(i)
            i -= 1


if __name__ == '__main__':
    min_heap = MinHeap()
    ll = [2, 7, 26, 25, 19, 17, 1, 90, 3, 36]
    random.shuffle(ll)
    print(ll)
    # for i in ll:
    #     min_heap.insert(i)
    print(min_heap.build_heap(ll))
    min_heap.del_min()
    print(min_heap.heap_list)
