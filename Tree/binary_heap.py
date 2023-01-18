#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
binary heap implementation by list
parent index = n
left child index = 2n
right child index = 2n + 1
"""

from random import randint


class BinaryHeap:
    def __init__(self, max_size, heap_type='min'):
        self.list = [None] * (max_size + 1)
        self.heap_size = 0  # size of binary heap
        self.max_size = max_size
        self.heap_type = heap_type

    def get_size(self):
        return self.heap_size

    def peek(self):
        return self.list[1]

    def level_order_traversal(self):
        for i in range(1, self.heap_size + 1):
            print(self.list[i])

    def insert(self, data):
        if self.is_full():  # full binary heap
            raise Exception('full binary heap')
        self.heap_size += 1  # size need to add 1 after inserting a new data
        index = self.heap_size
        self.list[index] = data  # add new node at the end of the binary heap
        parent_index = index // 2  # parent index of current node
        # check if the newly inserted node less or greater than its parent
        # otherwise we will swap it with its parent, until it less or greater
        # than its parent
        if self.heap_type == 'min':
            while parent_index > 0 and self.list[index] < self.list[parent_index]:
                # swap newly inserted node with its parent
                self.list[index], self.list[parent_index] = self.list[parent_index], self.list[index]
                index = index // 2
                parent_index = parent_index // 2
        else:
            while parent_index > 0 and self.list[index] > self.list[parent_index]:
                # swap newly inserted node with its parent
                self.list[index], self.list[parent_index] = self.list[parent_index], self.list[index]
                index = index // 2
                parent_index = parent_index // 2

    def is_empty(self):
        if self.heap_size == 0:
            return True
        return False

    def is_full(self):
        if self.heap_size + 1 == self.max_size:
            return True
        return False

    def extract(self):
        """ only the extraction of root node is allowed """
        if self.is_empty():
            raise Exception('empty binary heap')
        extract_node = self.list[1]
        # to maintain the property of binary heap, we need to put the last node at root
        # then swap it with its child if needed
        self.list[1], self.list[self.heap_size] = self.list[self.heap_size], None
        self.heap_size -= 1  # reduce heap_size after extraction
        index = 1  # current index
        while self.get_heapify_index(index) is not None:  # heapify
            child_index = self.get_heapify_index(index)
            self.list[index], self.list[child_index] = self.list[child_index], self.list[index]
            index = child_index
        return extract_node  # return root node

    def get_heapify_index(self, index):
        """
        get index of smaller or greater child
        :param index: parent index
        :return: index of smaller or greater child
        """
        if self.heap_size < 2 * index:  # parent has no child
            return None
        if self.heap_type == 'min':  # min heap
            # left child is smaller or has only left child
            if self.list[2 * index + 1] is None \
                    or self.list[2 * index] < self.list[2 * index + 1]:
                if self.list[index] < self.list[2 *
                                                index]:  # parent smaller than left child, no need to swap
                    return None
                else:  # parent greater than left child, swap them
                    return 2 * index
            else:  # right child is smaller
                if self.list[index] < self.list[2 * index + 1]:
                    return None
                else:  # parent greater than right child, swap them
                    return 2 * index + 1
        else:  # max heap
            # left child is greater or has only left child
            if self.list[2 * index + 1] is None \
                    or self.list[2 * index] > self.list[2 * index + 1]:
                if self.list[index] > self.list[2 *
                                                index]:  # parent greater than left child, no need to swap
                    return None
                else:  # parent smaller than left child, swap them
                    return 2 * index
            else:  # right child is greater
                if self.list[index] > self.list[2 * index + 1]:
                    return None
                else:  # parent smaller than right child, swap them
                    return 2 * index + 1

    def clear(self):
        """ delete entire binary heap """
        self.list = None


if __name__ == '__main__':
    my_heap = BinaryHeap(max_size=10, heap_type='min')
    my_list = [randint(1, 100) for i in range(1, 7)]
    print(my_list)
    for i in my_list:
        my_heap.insert(i)

    my_heap.extract()
    print(my_heap.list)
    my_heap.extract()
    print(my_heap.list)
    my_heap.extract()
    print(my_heap.list)
    my_heap.extract()
    print(my_heap.list)
    my_heap.extract()
    print(my_heap.list)
    my_heap.extract()
    print(my_heap.list)
