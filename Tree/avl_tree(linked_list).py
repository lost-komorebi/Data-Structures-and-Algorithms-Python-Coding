#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
from stack_and_queue.queue_by_linked_list import Queue
import sys
sys.path.append('../stack_and_queue')


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def insert_no_recursion(self, data):
        """ insertion by using loop """
        if self.root is None:  # empty tree
            self.root = Node(data)
            return
        prev = None
        cur = self.root
        while cur:  # loop until node has no left or right
            if data < cur.data:
                prev = cur
                cur = cur.left
            elif data > cur.data:
                prev = cur
                cur = cur.right
        if data < prev.data:  # compare data and insert
            prev.left = Node(data)
        else:
            prev.right = Node(data)

    def insert(self, cur, data):
        """ insert implementation by recursion """
        if self.root is None:  # empty tree
            self.root = Node(data)
            return
        else:
            if cur is None:
                cur = Node(data)
            elif data < cur.data:
                cur.left = self.insert(cur.left, data)
            else:
                cur.right = self.insert(cur.right, data)
            return cur

    def pre_order_traversal(self, root):
        """ root >>> left >>> right """
        print(root.data)
        if root.left:
            self.pre_order_traversal(root.left)
        if root.right:
            self.pre_order_traversal(root.right)

    def in_order_traversal(self, root):
        """ left >>> root >>> right """
        if root.left:
            self.in_order_traversal(root.left)
        print(root.data)
        if root.right:
            self.in_order_traversal(root.right)

    def post_order_traversal(self, root):
        """ left >>> right >>> root """
        if root.left:
            self.post_order_traversal(root.left)
        if root.right:
            self.post_order_traversal(root.right)
        print(root.data)

    def level_order_traversal(self, root):
        queue = Queue()
        queue.en_queue(root)
        while not queue.is_empty():
            root = queue.de_queue()
            print(root.data)
            if root.left is not None:
                queue.en_queue(root.left)
            if root.right is not None:
                queue.en_queue(root.right)

    def search(self, data):
        if self.root.data == data:
            return self.root
        cur = self.root
        if data < cur.data:
            while cur.left:
                if cur.left.data == data:
                    return cur.left
                else:
                    cur = cur.left
        else:
            while cur.right:
                if cur.right.data == data:
                    return cur.right
                else:
                    cur = cur.right
        return None


class AVLNode(Node):
    def __init__(self, data):
        super(AVLNode, self).__init__(data)
        self.height = 1  # set default height = 1


class AVL(BST):
    def __init__(self):
        super(AVL, self).__init__()

    def insert(self, root, data):
        # step 1 perform bst insertion
        if self.root is None:  # empty tree
            self.root = AVLNode(data)
            return
        if not root:
            return AVLNode(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
            #print(root.left.data)
        else:
            root.right = self.insert(root.right, data)

        # step 2 update height of all parent nodes
        # parent nodes' height equal to the highest child's height + 1
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        # step 3 get balance factor
        balance = self.get_balance(root)

        # step 4 check unbalanced node and try out rotations
        # case 1 left left condition
        if balance > 1 and data < root.left.data:
            return self.right_rotation(root)
        # case 2 right right condition
        if balance < -1 and data > root.right.data:
            return self.left_rotation(root)
        # case 3 left right condition
        if balance > 1 and data > root.left.data:
            root.left = self.left_rotation(root.left)
            return self.right_rotation(root)
        # case 4 right left condition
        if balance < -1 and data < root.right.data:
            root.right = self.right_rotation(root.right)
            return self.left_rotation(root)
        return root

    def right_rotation(self, unbalanced_node):
        # perform rotation
        new_node = unbalanced_node.left
        unbalanced_node.left = unbalanced_node.left.right
        new_node.right = unbalanced_node
        # update height
        unbalanced_node.height = 1 + \
            max(self.get_height(unbalanced_node.left), self.get_height(unbalanced_node.right))
        new_node.height = 1 + \
            max(self.get_height(new_node.left), self.get_height(new_node.right))
        return new_node

    def left_rotation(self, unbalanced_node):
        # perform rotation
        new_node = unbalanced_node.right
        unbalanced_node.right = unbalanced_node.right.left
        new_node.left = unbalanced_node
        # update height
        unbalanced_node.height = 1 + \
            max(self.get_height(unbalanced_node.left), self.get_height(unbalanced_node.right))
        new_node.height = 1 + \
            max(self.get_height(new_node.left), self.get_height(new_node.right))
        return new_node

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        """ get difference from left subtree and right subtree """
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)


if __name__ == '__main__':
    my_tree = BST()
    my_tree.insert(my_tree.root, 100)
    my_tree.insert(my_tree.root, 80)
    my_tree.insert(my_tree.root, 95)


    # my_tree.insert(my_tree.root, 11)
    # my_tree.insert(my_tree.root, 22)
    # my_tree.insert(my_tree.root, 33)
    # my_tree.insert(my_tree.root, 44)
    # my_tree.insert(my_tree.root, 55)
    #my_tree.insert(my_tree.root, 5)
    # print(my_tree.search(6))
    # my_tree.insert_no_recursion(10)
    # my_tree.insert_no_recursion(20)
    # my_tree.insert_no_recursion(30)
    # my_tree.insert_no_recursion(5)
    # print(my_tree.root.data)
    # print(my_tree.root.left.data)
    # print(my_tree.root.right.data)
    # print(my_tree.root.right.right.data)

    # my_tree.in_order_traversal(my_tree.root)
    # my_tree.post_order_traversal(my_tree.root)
    # my_tree.pre_order_traversal(my_tree.root)
    my_tree.level_order_traversal(my_tree.root)
