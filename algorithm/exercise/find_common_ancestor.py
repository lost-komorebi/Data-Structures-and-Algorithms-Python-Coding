#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree.
Avoid storing additional nodes in a data structure.
NOTE: This is not necessarily a binary search tree.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left
        self.parent = None


def insert(root, value):
    if not root:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def search(root, value):
    if not root:
        return
    if value < root.value:
        return search(root.left, value)
    elif value > root.value:
        return search(root.right, value)
    else:
        return root


def findFirstCommonAncestor(n1, n2, root):
    node_n1 = search(root, n1)
    node_n2 = search(root, n2)
    print(node_n1.parent.value, node_n2.parent.value)


def in_order_traversal(root: Node):
    if root.left:
        in_order_traversal(root.left)
    print(root.value)
    if root.right:
        in_order_traversal(root.right)


if __name__ == '__main__':
    my_tree = Node(100)
    my_list = [90, 110, 89, 91, 109, 111, 87, 93, 92, 94, 86, 88]
    for i in my_list:
        insert(my_tree, i)
    #in_order_traversal(my_tree)
    # for i in my_list:
    #     assert search(my_tree, i).value == i
    findFirstCommonAncestor(88, 93, my_tree)
