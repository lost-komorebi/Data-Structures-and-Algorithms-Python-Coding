#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
Write an algorithm to find the next node (i.e in-order successor) of given node in a binary search tree.
You may assume that each node has a link to its parent.
in-order successor is the node with the smallest value in the nodes greater than the value of input node
"""


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.parent = None


def insert(node, data):
    if node is None:
        return Node(data)
    else:
        if data <= node.data:
            temp = insert(node.left, data)
            node.left = temp
            temp.parent = node
        else:
            temp = insert(node.right, data)
            node.right = temp
            temp.parent = node
        return node


def in_order_successor(root, n: int):
    node = search(root, n)

    # n has right child, successor is the smallest in its right children
    if node.right:
        return find_minimum(root, node)

    # n has no right child, successor is one of its ancestors
    p = node.parent
    while p:
        if node == p.left:  # loop until current node is the left child of its parent
            return p
        node, p = p, p.parent
    return None  # last node has no successor


def find_minimum(root, node: Node):
    if not node.right.left:  # node.right has no left child, so node.right is successor
        return node.right
    cur = node.right.left  # node.right has left child
    while cur.left:  # traverse to left most child
        cur = cur.left
    return cur  # the left most child is successor


def search(root, n: int):
    if not root:
        return
    cur = root
    if n == root.data:
        return cur
    while cur:
        if n < cur.data:
            if cur.left:
                if n == cur.left.data:
                    return cur.left
                cur = cur.left
            else:
                return
        else:
            if cur.right:
                if n == cur.right.data:
                    return cur.right
                cur = cur.right
            else:
                return


def in_order_traversal(root):
    if not root:
        return
    if root.left:
        in_order_traversal(root.left)
    print(root.data)
    if root.right:
        in_order_traversal(root.right)


if __name__ == '__main__':
    my_tree = Node(100)
    my_list = [90, 110, 89, 91, 109, 111, 87, 93, 92, 94, 86, 88]
    my_list.append(100)  # add root node value

    for i in my_list:
        insert(my_tree, i)

    sorted_mylist = sorted(my_list)

    root = my_tree
    for i in my_list:
        assert search(root, i).data == i

    for i in sorted_mylist[:-1]:

        assert in_order_successor(
            root, i).data == sorted_mylist[sorted_mylist.index(i) + 1]
    # the successor of the last node in order traversal is Null
    assert not in_order_successor(root, sorted_mylist[-1])
