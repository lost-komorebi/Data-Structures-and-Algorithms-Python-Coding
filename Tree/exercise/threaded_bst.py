#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   threaded_bst.py
@Time    :   2023/03/12 13:37:21
@Author  :   komorebi 
'''
import random


class Node:
    def __init__(self, key, data, left=None, right=None, parent=None, successor=None) -> None:
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.successor = successor

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not self.left and not self.right

    def is_left_child(self):
        return self.parent and self.parent.left is self

    def is_right_child(self):
        return self.parent and self.parent.right is self

    def has_left_child(self):
        return self.left

    def has_right_child(self):
        return self.right

    def has_only_one_child(self):
        return (self.has_left_child() and not self.has_right_child()) or (not self.has_left_child() and self.has_right_child())

    def find_successor(self):
        """
        1. If the node has a right child, then the successor is the smallest key in the right subtree.
        2. If the node has no right child and is the left child of its parent, then the parent is the successor.
        3. If the node is the right child of its parent, and itself has no right child, 
        then the successor to this node is the successor of its parent, excluding this node.
        """
        successor = None
        if self.has_right_child():
            successor = self.right
            while successor.has_left_child():
                successor = successor.left
        else:
            if self.parent:
                if self.is_left_child():
                    successor = self.parent
                else:
                    self.parent.right = None
                    successor = self.parent.find_successor()
                    self.parent.right = self
        return successor

    def find_predecessor(self):
        """
        1. If the node has a left child, then the predecessor is the maximum key in the right subtree.
        2. If the node has no left child, from the node move up the towards the root unitl we encounter a node that is 
        the first right child ('P') we encountered. Then the parent of the right node ('P') is the predecessor, 
        otherwise there is no predecessor for the node.
        """
        predecessor = None
        if self.has_left_child():
            predecessor = self.left
            while predecessor.right:  # find the maximum value in left subtree
                predecessor = predecessor.right
        else:
            while self:  # move up until encounter a right child of its parent
                if self.is_right_child():
                    predecessor = self.parent
                    break
                else:
                    self = self.parent
        return predecessor

    def replace_node(self, key, data, left, right):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        if self.has_left_child():
            self.left.parent = self
        if self.has_right_child():
            self.right.parent = self
        #node.successor = node.find_successor()

    def splice_out(self):
        """ move successor to proper position """
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.has_only_one_child():
            if self.has_left_child():  # node only has left child
                self.left.parent = self.parent
                if self.is_left_child():  # node is left child of its parent
                    self.parent.left = self.left
                elif self.is_right_child():  # node is right child of its parent
                    self.parent.right = self.left
            else:  # node only has right child
                self.right.parent = self.parent
                if self.is_left_child():  # node is left child of its parent
                    self.parent.left = self.right
                elif self.is_right_child():  # node is right child of its parent
                    self.parent.right = self.right


class BST:
    def __init__(self) -> None:
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def put(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
            self.size += 1
        else:
            self._put(key, value, self.root)

    def _put(self, key, value, cur):
        if key < cur.key:
            if cur.left:
                self._put(key, value, cur.left)
            else:
                node = Node(key, value)
                cur.left = node
                node.parent = cur
                # when we add a node, we need to update successor of itself and its predecessor
                node.successor = node.find_successor()  # update successor of itself
                pred = node.find_predecessor()  # find predecessor
                if pred:  # update successor of its predecessor
                    pred.successor = pred.find_successor()
                self.size += 1
        elif key > cur.key:
            if cur.right:
                self._put(key, value, cur.right)
            else:
                node = Node(key, value)
                cur.right = node
                node.parent = cur
                # when we add a node, we need to update successor of itself and its predecessor
                node.successor = node.find_successor()  # update successor of itself
                pred = node.find_predecessor()  # find predecessor
                if pred:  # update successor of its predecessor
                    pred.successor = pred.find_successor()
                self.size += 1
        else:  # if we meet duplicate key, just updata the payload
            cur.data = value

    def __setitem__(self, key, data):
        self.put(key, data)

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
        if self.size == 0:
            return
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

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        node = self.get(key)
        if node:
            return True
        return False

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
                # when we delete a node, we just need to update successor of its predecessor
                pred = node.find_predecessor()  # find predecessor
                self._delete(node)
                if pred:  # update successor of predecessor
                    pred.successor = pred.find_successor()
            self.size -= 1

    def _delete(self, node: Node):
        # 1. node need to be deleted has no child
        if node.is_leaf():
            if node.is_left_child():
                node.parent.left = None
            else:
                node.parent.right = None
        # 2. node need to be deleted has one child
        elif node.has_only_one_child():
            if node.has_left_child():  # node only has left child
                if node.is_left_child():  # node is left child of its parent
                    node.left.parent = node.parent
                    node.parent.left = node.left
                elif node.is_right_child():  # node is right child of its parent
                    node.left.parent = node.parent
                    node.parent.right = node.left
                else:  # node is root
                    node.replace_node(
                        node.left.key, node.left.data, node.left.left, node.left.right)
            else:  # node only has right child
                if node.is_left_child():  # node is left child of its parent
                    node.right.parent = node.parent
                    node.parent.left = node.right
                elif node.is_right_child():  # node is right child of its parent
                    node.right.parent = node.parent
                    node.parent.right = node.right
                else:  # node is root
                    node.replace_node(
                        node.right.key, node.right.data, node.right.left, node.right.right)
        # 3. node need to be deleted has two children
        else:
            successor = node.find_successor()
            successor.splice_out()
            # replace key and data
            node.key = successor.key
            node.data = successor.data

    def __delitem__(self, key):
        self.delete(key)

    def in_order_traversal_non_recursion(self):
        """
        left > root > right
        Using the findSuccessor method, write a non-recursive inorder traversal for a binary search tree.
        """
        cur = self.root
        if cur:
            while cur.has_left_child():
                cur = cur.left
            print(cur.key)
            successor = cur.find_successor()
            while successor:
                print(successor.key)
                successor = successor.find_successor()

    def in_order_traversal_recursion(self, root):
        """ left > root > right, from small key to big key """
        if not root:
            return
        if root.left:
            self.in_order_traversal_recursion(root.left)
        print(root.key)
        if root.right:
            self.in_order_traversal_recursion(root.right)


if __name__ == '__main__':
    bst = BST()
    ll = list(random.sample(range(1, 100), 15))

    for i in ll:
        bst[i] = str(i)

    print(len(bst))

    for i in ll:
        del bst[i]

    bst[92] = '92'
    print(92 in bst)
    bst[92] = '96'
    print(bst[92].data)
    del bst[92]
    print(92 in bst)
