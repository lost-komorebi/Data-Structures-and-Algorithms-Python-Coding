#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
for a easy mathmatics calculation, we will not insert node at the 0 index
root_node index = x, hence left index = 2x, right index = 2x + 1
"""


class BST:
    def __init__(self, max_size):
        self.list = max_size * [None]
        self.max_size = max_size
        self.max_used_index = 0

    def insert(self, data, index=1):
        """
        add new element to bst
        :param data:
        :param index: temporary variable for recursion
        :return: no return if inserted successfully, else raise exception
        """
        if self.max_used_index == 0:
            self.list[1] = data
            self.max_used_index += 1
        else:
            if data <= self.list[index]:  # left side
                if 2 * index > self.max_size:
                    raise Exception('full binary search list')
                if self.list[2 *
                             index] is not None:  # compare date and left recursively
                    self.insert(data, 2 * index)
                else:
                    self.list[2 * index] = data
                    if self.max_used_index < 2 * index:
                        self.max_used_index = 2 * index
            else:  # right side
                if 2 * index + 1 >= self.max_size:
                    raise Exception('full binary search list')
                if self.list[2 * index +
                             1] is not None: # compare date and right recursively
                    self.insert(data, 2 * index + 1)
                else:
                    self.list[2 * index + 1] = data
                    if self.max_used_index < 2 * index + 1:
                        self.max_used_index = 2 * index + 1

    def level_order_traversal(self):
        """ print all elements from level 1 to the highest level """
        start = 1
        end = self.max_used_index + 1
        for i in range(start, end):
            if self.list[i] is not None:
                print(self.list[i])

    def in_order_traversal(self, index=1):
        """ left >>> root >>> right  print ascending """
        if index > self.max_used_index:
            return
        self.in_order_traversal(2 * index)
        if self.list[index] is not None:
            print(self.list[index])
        self.in_order_traversal(2 * index + 1)

    def pre_order_traversal(self, index=1):
        """ root >>> left >>> right """
        if index > self.max_used_index:
            return
        if self.list[index] is not None:
            print(self.list[index])
        self.pre_order_traversal(2 * index)
        self.pre_order_traversal(2 * index + 1)

    def post_order_traversal(self, index=1):
        """ left >>> right >>> root """
        if index > self.max_used_index:
            return
        self.post_order_traversal(2 * index)
        self.post_order_traversal(2 * index + 1)
        if self.list[index] is not None:
            print(self.list[index])

    def clear(self):
        """ delete entire binary search tree """
        self.list = None

    def delete(self, data):
        if self.list is None:
            raise Exception('empty bst')
        start = 1
        end = self.max_used_index + 1
        for i in range(start, end):
            if self.list[i] == data:
                temp = self.list[i]
                self.list[i] = None
                return temp
        raise Exception(f'bst.delete({data}): {data} not in list')

    def search(self, data, index=1):
        if self.list is None:
            return None
        if self.list[index] == data:
            return self.list[index]
        if data < self.list[index]:
            if self.list[2 * index]:
                if data == self.list[2 * index]:
                    return self.list[2 * index]
                else:
                    return self.search(data, index * 2)
        if data > self.list[index]:
            if self.list[2 * index + 1]:
                if data == self.list[2 * index + 1]:
                    return self.list[2 * index + 1]
                else:
                    return self.search(data, 2 * index + 1)


if __name__ == '__main__':
    my_tree = BST(100)
    for _ in [80, 50, 90, 30, 60, 20, 40, 95, 100, 101, 85, 84, 35, 45, 66]:
        my_tree.insert(_)
    print(my_tree.delete(101))
    print(my_tree.in_order_traversal())
