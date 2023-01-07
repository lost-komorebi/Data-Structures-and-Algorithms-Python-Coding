#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
for a easy mathmatics calculation, we will not insert node at the 0 index
root_node index = x, hence left index = 2x, right index = 2x + 1
"""


class BinaryTree:
    def __init__(self, max_size):
        self.max_size = max_size
        self.tree = max_size * [None]
        self.last_used_index = 0

    def append(self, data):
        """ add a new node to the binary tree """
        if self.last_used_index == self.max_size - 1:
            raise Exception('full binary tree')
        self.tree[self.last_used_index + 1] = data
        self.last_used_index += 1

    def search(self, data):
        """ using level order traversal to find node """
        start = 1  # we will leave index 0 as empty
        end = self.last_used_index + 1
        for i in range(start, end):
            if self.tree[i] == data:
                return self.tree[i]
        return None

    def level_order_traversal(self):
        start = 1  # we will leave index 0 as empty
        end = self.last_used_index + 1
        for i in range(start, end):
            print(self.tree[i])

    def pre_order_traversal(self, start=1):  # we will leave index 0 as empty
        if start > self.last_used_index:
            return
        print(self.tree[start])
        self.pre_order_traversal(2 * start)
        self.pre_order_traversal(2 * start + 1)

    def in_order_traversal(self, start=1):  # we will leave index 0 as empty
        if start > self.last_used_index:
            return
        self.in_order_traversal(2 * start)
        print(self.tree[start])
        self.in_order_traversal(2 * start + 1)

    def post_order_traversal(self, start=1):  # we will leave index 0 as empty
        if start > self.last_used_index:
            return
        self.post_order_traversal(2 * start)
        self.post_order_traversal(2 * start + 1)
        print(self.tree[start])

    def delete(self, data):
        if self.last_used_index == 0:
            raise Exception('delete from empty tree')
        start = 1
        end = self.last_used_index + 1
        for i in range(start, end):
            if self.tree[i] == data:
                self.tree[i] = self.tree[self.last_used_index]
                self.tree[self.last_used_index] = None
                self.last_used_index -= 1
                return

    def clear(self):
        """ delete entire tree """
        self.tree = None


if __name__ == '__main__':
    my_tree = BinaryTree(40)
    my_tree.append('n1')
    my_tree.append('n2')
    my_tree.append('n3')
    my_tree.append('n4')
    my_tree.append('n5')
    my_tree.append('n6')
    my_tree.append('n7')
    my_tree.append('n8')
    my_tree.append('n9')
    my_tree.append('n10')
    my_tree.delete('n3')
    print(my_tree.level_order_traversal())
