#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth
(ie , if you have a tree with depth D, you’ll have D linked lists)
"""


class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

    def add(self, val):
        if self.next is None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)

    def __str__(self):
        return "({val})".format(val=self.val) + str(self.next)


class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None




def depth(tree: BinaryTree):
    if not tree.val:
        return
    q = [tree]
    visited = []
    while q:
        cur = q.pop(0)
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
        visited.append(cur)


def treeToLinkedList(tree, custDict={}, d=None):
    pass


if __name__ == '__main__':
    pass
