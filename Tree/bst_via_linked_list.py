#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
using linked list to perform binary search tree
in the left subtree node's value is less to its parent node's value
in the right subtree node's value is greater than it's parent node's value
"""

__author__ = 'komorebi'
from stack_and_queue.queue_by_linked_list import Queue
import sys
sys.path.append('..')


class BSTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def clear(self):
        """ delete entire tree """
        self.data = None
        self.left = None
        self.right = None

    def insert_node(self, node_data):
        if self.data is None:
            self.data = node_data
            return
        if node_data < self.data:
            if self.left is None:
                self.left = BSTNode(node_data)
                return
            self.left.insert_node(node_data)
        if node_data > self.data:
            if self.right is None:
                self.right = BSTNode(node_data)
                return
            self.right.insert_node(node_data)

    def pre_order_traversal(self):
        """ root >>> left >>> right """
        print(self.data)
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    def in_order_traversal(self):
        """ left >>> root >>> right """
        if self.left:
            self.left.in_order_traversal()
        print(self.data)
        if self.right:
            self.right.in_order_traversal()

    def post_order_traversal(self):
        """ left >>> right >>> root """
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.data)

    def level_order_traversal(self):
        queue = Queue()
        queue.en_queue(self)
        while not queue.is_empty():
            root = queue.de_queue()
            print(root.data)
            if root.left is not None:
                queue.en_queue(root.left)
            if root.right is not None:
                queue.en_queue(root.right)

    def search(self, node_data):
        if self.data is None:
            return None
        if self.data == node_data:
            return self.data
        elif node_data < self.data:
            if self.left is not None:
                if self.left.data == node_data:
                    return self.left.data
                return self.left.search(node_data)
        else:
            if self.right is not None:
                if self.right.data == node_data:
                    return self.right.data
                return self.right.search(node_data)
        return None

    def delete(self, data_to_delete):
        if self.data is None:
            raise Exception('empty binary search tree')
        # find the node to delete
        if data_to_delete < self.data:
            if self.left:
                self.left = self.left.delete(data_to_delete)
            else:
                raise Exception(
                    f"bst.delete({data_to_delete}): {data_to_delete} not in bst")
        if data_to_delete > self.data:
            if self.right:
                self.right = self.right.delete(data_to_delete)
            else:
                raise Exception(
                    f"bst.delete({data_to_delete}): {data_to_delete} not in bst")
        else:
            # delete node which has zero or one child
            if self.left is None:
                temp = self.right
                self.left = None
                return temp
            if self.right is None:
                temp = self.left
                self.right = None
                return temp
            # find the greatest node in the left subtree
            node = self.left
            while node.right:
                node = node.right
            self.data = node.data  # replace date with the greatest node in the left subtree
            self.left = self.left.delete(node.data)
        return self


if __name__ == '__main__':
    my_tree = BSTNode(None)

    for _ in [80, 50, 90, 30, 60, 20, 40, 95, 100, 101, 85, 84, 35, 45, 66]:
        my_tree.insert_node(_)
    my_tree.delete(80)
    print(my_tree.level_order_traversal())
