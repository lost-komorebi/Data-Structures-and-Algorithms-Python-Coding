#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.
To build a binary search tree with minimal height
we can assume the sorted array inorder traversal of a tree
as we know, the order of inorder traversal is left, root, right
so we can choose the middle element as root
then use same approach on it's left and right side recursively
"""

class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def minimal_tree(li: list) -> BSTNode:
    length = len(li)
    if length == 0:
        return 
    mid = length // 2
    root = BSTNode(li[mid])
    root.left = minimal_tree(li[0: mid])
    root.right = minimal_tree(li[mid + 1:])
    return root




if __name__ == '__main__':
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    my_tree = minimal_tree(sorted_array)