#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   parse_tree.py
@Time    :   2023/03/03 09:30:56
@Author  :   komorebi 
'''

"""
implement a parse tree by using a tree data structure
rules:
1. If the current token is a '(', add a new node as the left child of the current node, 
and descend to the left child.
2. If the current token is a number, 
set the root value of the current node to the number and return to the parent.
3. If the current token is in the list ['+','−','/','*'], 
set the root value of the current node to the operator represented by the current token. 
Add a new node as the right child of the current node and descend to the right child.
4. If the current token is a ')', go to the parent of the current node.
"""


class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        return self.stack_list.pop()


class BinaryTree:
    def __init__(self, data=None) -> None:
        self.key = data
        self.left = None
        self.right = None

    def insert_left(self, new_data):
        if self.left is None:
            self.left = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data)
            t.left = self.left
            self.left = t

    def insert_right(self, new_data):
        if self.right is None:
            self.right = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data)
            t.right = self.right
            self.right = t

    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

    def post_order_traversal(self):
        """ left > right > root """
        if self.get_left_child():
            self.get_left_child().post_order_traversal()
        if self.get_right_child():
            self.get_right_child().post_order_traversal()
        print(self.get_root_val())


def build_parse_tree(expression):
    exp_list = expression.split()
    exp_stack = Stack()
    exp_tree = BinaryTree('')
    exp_stack.push(exp_tree)
    current_tree = exp_tree
    for i in exp_list:
        if i == '(':  # rule 1
            current_tree.insert_left('')
            exp_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif is_number(i):  # rule 2
            current_tree.set_root_val(i)
            current_tree = exp_stack.pop()
        elif i in '+-*/':  # rule 3
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            exp_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':  # rule 4
            current_tree = exp_stack.pop()
        else:
            raise ValueError
    return exp_tree


def is_number(i):
    """ check if a string is number """
    if i.isdigit():
        return True
    if i.replace('.', '').replace('-', '').isdigit():
        return True
    return False


def evaluate(tree: BinaryTree):
    """ evaluate the parse tree """
    left = tree.get_left_child()
    right = tree.get_right_child()
    if left and right:  # if a node has left and right, so this node must be a operator
        fn = tree.get_root_val()
        return str(eval(evaluate(left) + fn + evaluate(right)))
    else:  # leaf noede
        return tree.get_root_val()


if __name__ == '__main__':
    exp = '( 3 + ( ( 4 * 5 ) / 2 ) )'
    print(build_parse_tree(exp).post_order_traversal())
    print(evaluate(build_parse_tree(exp)))
