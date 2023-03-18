#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree.
Avoid storing additional nodes in a data structure.
NOTE: This is not necessarily a binary search tree.
"""
"""
solution:
only when n1, n2 locate in different sides of root, then the root is the first common ancestor of n1 and n2
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def find_node_in_tree(root, node):
    """ if a node exists in a tree, return True; else, return False """
    if not root:
        return False
    if root == node:
        return True
    else:  # recursively find in left subtree or right subtree
        return (find_node_in_tree(root.left, node)) or (find_node_in_tree(root.right, node))


def find_common_ancestor(n1, n2, root):
    n1_in_tree = find_node_in_tree(root.left, n1)
    n2_in_tree = find_node_in_tree(root.left, n2)
    # when n1 and n2 locate in different side of a node,the node is first common ancestor
    if n1_in_tree ^ n2_in_tree:  # operator ^ means only one is True then it will return True
        return root
    else:  # find first comman ancestor recursively
        if n1_in_tree:
            return find_common_ancestor(n1, n2, root.left)
        else:
            return find_common_ancestor(n1, n2, root.right)


if __name__ == '__main__':
    my_tree = Node(55)
    node_44 = Node(44)
    node_77 = Node(77)
    node_22 = Node(22)
    node_99 = Node(99)
    node_35 = Node(35)
    node_88 = Node(88)
    node_90 = Node(90)
    node_95 = Node(95)
    node_54 = Node(54)
    node_33 = Node(33)
    my_tree.left = node_44
    my_tree.right = node_77
    node_44.left = node_22
    node_44.right = node_99
    node_22.left = node_35
    node_22.right = node_88
    node_88.left = node_54
    node_99.left = node_90
    node_99.right = node_95
    node_90.right = node_33

    print(find_common_ancestor(node_54, node_88, my_tree))
