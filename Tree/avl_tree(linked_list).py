#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


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
        queue = []
        queue.append(root)
        while queue:
            root = queue.pop(0)
            print(root.data)
            if root.left is not None:
                queue.append(root.left)
            if root.right is not None:
                queue.append(root.right)

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

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root: AVLNode, data) -> AVLNode:
        # step 1 perform bst insertion
        if not root:
            return AVLNode(data)
        elif data < root.data:
            # left subtree equal to left subtree after insertion of new node
            root.left = self._insert(root.left, data)
        else:
            # right subtree equal to right subtree after insertion of new node
            root.right = self._insert(root.right, data)

        # step 2 update height of root node
        root.height = self.get_height(root)
        #root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # step 3 get balance factor
        balance = self.get_balance(root)

        # step 4 check unbalanced node and try out rotations
        # case 1 left left condition(root node is left heavy and we insert a new node at left side of root.left)
        if balance > 1 and data < root.left.data:
            return self.right_rotation(root)
        # case 2 right right condition(root node is right heavy and we insert a new node at right side of root.right)
        if balance < - 1 and data > root.right.data:
            return self.left_rotation(root)
        # case 3 left right condition(root node is left heavy and we insert a new node at right side of root.left)
        if balance > 1 and data > root.left.data:
            root.left = self.left_rotation(root.left)
            return self.right_rotation(root)
        # case 4 right left condition(root node is right heavy and we insert a new node at left side of root.right)
        if balance < -1 and data < root.right.data:
            root.right = self.right_rotation(root.right)
            return self.left_rotation(root)
        return root

    def right_rotation(self, unbalanced_node):
        new_root = unbalanced_node.left
        unbalanced_node.left = new_root.right
        new_root.right = unbalanced_node
        # update height of unbalance_node and new_root
        unbalanced_node.height = self.get_height(unbalanced_node)
        new_root.height = self.get_height(new_root)
        return new_root

    def left_rotation(self, unbalanced_node):
        new_root = unbalanced_node.right
        unbalanced_node.right = new_root.left
        new_root.left = unbalanced_node
        # update height of unbalance_node and new_root
        unbalanced_node.height = self.get_height(unbalanced_node)
        new_root.height = self.get_height(new_root)
        return new_root

    def get_height(self, root):
        if not root:
            return 0
        # node's height equal to the height of higher child plus one
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

    def get_balance(self, root):
        """ get difference from left subtree and right subtree """
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)


def pretty_print_tree(root):
    """
    This function pretty prints a binary tree
    :param root: root of tree
    :return: none
    """
    lines, _, _, _ = _pretty_print_tree(root)
    for line in lines:
        print(line)


def _pretty_print_tree(root):
    """
    Code credits: Stack overflow
    :param root: root of tree
    :return: none
    """
    if root.right is None and root.left is None:
        line = '%s' % root.data
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if root.right is None:
        lines, n, p, x = _pretty_print_tree(root.left)
        s = '%s' % root.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if root.left is None:
        lines, n, p, x = _pretty_print_tree(root.right)
        s = '%s' % root.data
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _pretty_print_tree(root.left)
    right, m, q, y = _pretty_print_tree(root.right)
    s = '%s' % root.data
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * \
        '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + \
        (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + \
        [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


if __name__ == '__main__':
    ll = [40, 20, 10, 25, 30, 22, 50]

    my_tree = AVL()
    for i in ll:
        my_tree.insert(i)

    pretty_print_tree(my_tree.root)
