#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.
"""


class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def insert(self, k):
        if not self.root:
            self.root = BSTNode(k)
        else:
            cur = self.root
            if k < cur.data:
                if cur.left:
                    while cur.left:
                        if k < cur.left.data:
                            cur = cur.left
                        else:
                            cur.right = BSTNode(k)
                    cur.left = BSTNode(k)
                else:
                    cur.left = BSTNode(k)
            else:
                if cur.right:
                    while cur.right:
                        if k > cur.right.data:
                            cur = cur.right
                        else:
                            cur.left = BSTNode(k)
                    cur.right = BSTNode(k)
                else:
                    cur.right = BSTNode(k)

    def level_order_traversal(self):
        if not self.root:
            return
        q = [self.root]
        visited = []
        while q:
            cur = q.pop(0)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            visited.append(cur.data)
        print(visited)


def minimal_tree(sorted_array):
    pass


if __name__ == '__main__':
    #sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sorted_array = [5,4,2,3]
    my_bst = BST()
    for i in sorted_array:
        my_bst.insert(i)
    my_bst.level_order_traversal()
