#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   threaded_bst.py
@Time    :   2023/03/12 13:37:21
@Author  :   komorebi 
'''
import random


class Node:
    def __init__(self, key, data) -> None:
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.successor = None

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not self.left and not self.right

    def is_left_child(self):
        return self.parent.left is self

    def is_right_child(self):
        return self.parent.right is self

    def has_left_child(self):
        return self.left

    def has_right_child(self):
        return self.right

    def has_only_one_child(self):
        return (self.has_left_child() and not self.has_right_child()) or (not self.has_left_child() and self.has_right_child())


class BST:
    def __init__(self) -> None:
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def put(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._put(key, value, self.root)
        self.size += 1

    def _put(self, key, value, cur):
        if key < cur.key:
            if cur.left:
                self._put(key, value, cur.left)
            else:
                node = Node(key, value)
                cur.left = node
                node.parent = cur
        else:
            if cur.right:
                self._put(key, value, cur.right)
            else:
                node = Node(key, value)
                cur.right = node
                node.parent = cur

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
            visited.append(cur.key)
        return (visited)

    def get(self, key):
        if self.root.key == key:
            return self.root
        else:
            return self._get(key, self.root)

    def _get(self, key, cur: Node):
        if not cur:
            return
        if key == cur.key:
            return cur
        if key < cur.key:
            return self._get(key, cur.left)
        else:
            return self._get(key, cur.right)

    def delete(self, key):
        if self.size == 0:
            raise IndexError('delete from empty tree')
        node = self.get(key)
        if not node:
            raise KeyError(f'{key} not in bst')
        else:
            if self.size == 1 and self.root.key == key:  # delete root node in a tree has only root node
                self.root = None
            else:
                self._delete(node)
            self.size -= 1

    def _delete(self, node: Node):
        # 1. node need to be deleted has no child
        if node.is_leaf():
            node.parent = None
            if node.is_left_child():
                node.parent.left = None
            else:
                node.parent.right = None
        # 2. node need to be deleted has one child
        elif node.has_only_one_child():
            if node.is_root():  # node need to be deleted is root node
                if node.has_left_child():
                    self.root = node.left
                    node.left.parent = None
                else:
                    self.root = node.right
                    node.right.parent = None
            else:  # node need to be deleted is not root node
                if node.is_left_child():  # node is left child of its parent
                    if node.has_left_child():  # node only has left child
                        node.left.parent = node.parent
                        node.parent.left = node.left
                    else:  # node only has right child
                        node.right.parent = node.parent
                        node.parent.left = node.right
                else:  # node is right child of its parent
                    if node.has_left_child():  # node only has left child
                        node.left.parent = node.parent
                        node.parent.right = node.left
                    else:  # node only has right chiild
                        node.right.parent = node.parent
                        node.parent.right = node.right
        # 3. node need to be deleted has two children
        else:
            successor = self.find_successor(node)
            if node.is_root():  # node need to be deleted is root node
                if successor.is_leaf():
                    node.right = None
                node.left.parent = successor
                successor.left = node.left
                self.root = successor
                successor.parent = None
            else:  # node need to be deleted is not root node
                if successor.is_leaf():  # successor is leaf node
                    if successor.is_left_child():
                        successor.parent.left = None
                    else:
                        successor.parent.right = None
                # according to the rule to find successor, successor has no left child
                # so we don't need to consider that situation
                elif successor.has_right_child():  # successor has right child
                    successor.right.parent = successor.parent
                    if successor.is_left_child():  # successor is left child
                        successor.parent.left = successor.right
                    elif successor.is_right_child():  # successor is right child
                        successor.parent.right = successor.right
                # replace key and data
                node.key = successor.key
                node.data = successor.data

    def find_successor(self, node: Node) -> Node:
        """ 
        find the smallest node from current node's right child, i.e. the left most node in its right child
        current node must has two children, otherwise we don't need to find the successor
        """
        if node.right.left:
            cur = node.right.left
            while cur.left:
                cur = cur.left
            return cur
        else:
            return node.right


if __name__ == '__main__':
    bst = BST()
    ll = [2, 0, 7, 26, 25, 19, 17, 1, 90, 3, 36, 18]
    # random.shuffle(ll)
    for i in ll:
        bst.put(i, str(i))

    print(bst.level_order_traversal())
