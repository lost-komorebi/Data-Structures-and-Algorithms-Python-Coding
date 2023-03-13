#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   threaded_bst_unittest.py
@Time    :   2023/03/12 22:06:01
@Author  :   komorebi 
'''

import unittest
from threaded_bst import BST


class TestBST(unittest.TestCase):
    def test_case1(self):
        """ delete from a empty tree """
        bst = BST()
        with self.assertRaises(IndexError):
            bst.delete(1)

    def test_case2(self):
        """ delete a non exist node """
        bst = BST()
        bst.put(1, '1')
        with self.assertRaises(KeyError):
            bst.delete(2)

    def test_case3(self):
        """ tree only has root, and root is the node need to be deleted """
        bst = BST()
        ll = [2]
        for i in ll:
            bst.put(i, str(i))
        bst.delete(2)
        self.assertEqual(bst.root, None)

    def test_case4(self):
        """ delete root node from a tree only has root and root.left """
        bst = BST()
        ll = [2, 1]
        for i in ll:
            bst.put(i, str(i))
        bst.delete(2)
        self.assertEqual(bst.root.key, 1)
        self.assertEqual(bst.root.left, None)
        self.assertEqual(bst.root.right, None)
        self.assertEqual(bst.level_order_traversal(), [1])

    def test_case5(self):
        """ delete root node from a tree only has root and root.right """
        bst = BST()
        ll = [2, 7]
        for i in ll:
            bst.put(i, str(i))
        bst.delete(2)
        self.assertEqual(bst.root.key, 7)
        self.assertEqual(bst.root.left, None)
        self.assertEqual(bst.root.right, None)
        self.assertEqual(bst.level_order_traversal(), [7])

    def test_case6(self):
        """ delete a non root left node which only has left node from a tree """
        bst = BST()
        ll = [2, 1, 7, 26, 25, 19, 17, 90, 3, 36, 0]
        for i in ll:
            bst.put(i, str(i))
        bst.delete(1)
        self.assertEqual(bst.root.key, 2)
        self.assertEqual(bst.root.left.key, 0)
        self.assertEqual(bst.root.right.key, 7)
        self.assertEqual(bst.level_order_traversal(), [
                         2, 0, 7, 3, 26, 25, 90, 19, 36, 17])

    def test_case7(self):
        """ delete a non root left node which only has right node from a tree """
        bst = BST()
        ll = [2, 0, 7, 26, 25, 19, 17, 1, 90, 3, 36]
        for i in ll:
            bst.put(i, str(i))
        bst.delete(0)
        self.assertEqual(bst.root.key, 2)
        self.assertEqual(bst.root.left.key, 1)
        self.assertEqual(bst.root.right.key, 7)
        self.assertEqual(bst.level_order_traversal(), [
                         2, 1, 7, 3, 26, 25, 90, 19, 36, 17])

    def test_case8(self):
        """ delete a non root right node which only has left node from a tree """
        bst = BST()
        ll = [2, 0, 7, 26, 25, 19, 17, 1, 90, 3, 36]
        for i in ll:
            bst.put(i, str(i))
        bst.delete(90)
        self.assertEqual(bst.root.key, 2)
        self.assertEqual(bst.root.left.key, 0)
        self.assertEqual(bst.root.right.key, 7)
        self.assertEqual(bst.level_order_traversal(), [
                         2, 0, 7, 1, 3, 26, 25, 36, 19, 17])

    def test_case9(self):
        """ delete a non root right node which only has right node from a tree """
        bst = BST()
        ll = [2, 0, 7, 26, 25, 19, 17, 1, 90, 3, 91]
        for i in ll:
            bst.put(i, str(i))
        bst.delete(90)
        self.assertEqual(bst.root.key, 2)
        self.assertEqual(bst.root.left.key, 0)
        self.assertEqual(bst.root.right.key, 7)
        self.assertEqual(bst.level_order_traversal(), [
                         2, 0, 7, 1, 3, 26, 25, 91, 19, 17])

    def test_case10(self):
        """ 
        delete a root node which has left and right children from a tree
        successor is a leaf node 
        """
        bst = BST()
        ll = [2, 1, 7, 8]
        for i in ll:
            bst.put(i, str(i))
        bst.delete(2)
        self.assertEqual(bst.root.key, 7)
        self.assertEqual(bst.root.left.key, 1)
        self.assertEqual(bst.root.right.key, 8)
        self.assertEqual(bst.level_order_traversal(), [
                         7, 1, 8])

    def test_case11(self):
        """ 
        delete a root node which has left and right children from a tree
        successor is not a leaf node 
        """
        bst = BST()
        ll = [2, 1, 7]
        for i in ll:
            bst.put(i, str(i))
        bst.delete(2)
        self.assertEqual(bst.root.key, 7)
        self.assertEqual(bst.root.left.key, 1)
        self.assertEqual(bst.root.right, None)
        self.assertEqual(bst.level_order_traversal(), [
                         7, 1])

    def test_case12(self):
        """
        delete a non root node which has left and right children from a tree
        successor is a leaf left node 
        """
        bst = BST()
        ll = [2, 0, 7, 26, 25, 19, 17, 1, 90, 3, 36]
        for i in ll:
            bst.put(i, str(i))
        bst.delete(7)
        self.assertEqual(bst.root.key, 2)
        self.assertEqual(bst.root.left.key, 0)
        self.assertEqual(bst.root.right.key, 17)
        self.assertEqual(bst.level_order_traversal(), [
                         2, 0, 17, 1, 3, 26, 25, 90, 19, 36])

    def test_case13(self):
        """
        delete a non root node which has left and right children from a tree
        successor is a leaf right node 
        """
        bst = BST()
        ll = [2, 0, 7, 26, 25, 19, 17, 1, 90, 3, 91]
        for i in ll:
            bst.put(i, str(i))
        bst.delete(26)
        self.assertEqual(bst.root.key, 2)
        self.assertEqual(bst.root.left.key, 0)
        self.assertEqual(bst.root.right.key, 7)
        self.assertEqual(bst.level_order_traversal(), [
                         2, 0, 7, 1, 3, 90, 25, 91, 19, 17])

    def test_case14(self):
        """
        delete a non root node which has left and right children from a tree
        successor is a right node has right child
        """
        bst = BST()
        ll = [2, 0, 7, 26, 25, 19, 17, 1, 90, 3, 91]
        for i in ll:
            bst.put(i, str(i))
        bst.delete(26)
        self.assertEqual(bst.root.key, 2)
        self.assertEqual(bst.root.left.key, 0)
        self.assertEqual(bst.root.right.key, 7)
        self.assertEqual(bst.level_order_traversal(),
                         [2, 0, 7, 1, 3, 90, 25, 91, 19, 17])

    def test_case15(self):
        """
        delete a non root node which has left and right children from a tree
        successor is a left node has right child
        """
        bst = BST()
        ll = [2, 0, 7, 26, 25, 19, 17, 1, 90, 3, 36, 18]
        for i in ll:
            bst.put(i, str(i))
        bst.delete(7)
        self.assertEqual(bst.root.key, 2)
        self.assertEqual(bst.root.left.key, 0)
        self.assertEqual(bst.root.right.key, 17)
        self.assertEqual(bst.level_order_traversal(), [
                         2, 0, 17, 1, 3, 26, 25, 90, 19, 36, 18])


if __name__ == '__main__':
    unittest.main()
