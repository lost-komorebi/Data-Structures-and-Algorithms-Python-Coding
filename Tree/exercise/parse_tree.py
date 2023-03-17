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
3. If the current token is in the list ['+','−','/','*','and','or'], 
set the root value of the current node to the operator represented by the current token. 
Add a new node as the right child of the current node and descend to the right child.
4. If the current token is a ')', go to the parent of the current node.
5. If the current token is a 'not', go to the parent of the current node. Then do same operations
with rule 3
"""




import operator
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
    exp_list = exp_split(expression)
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
        elif i in ['+', '-', '*', '/', 'and', 'or']:  # rule 3
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            exp_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':  # rule 4 go to the parent of current node
            current_tree = exp_stack.pop()
        elif i in ['not']:  # rule 5
            current_tree = exp_stack.pop()
            current_tree.set_root_val(i)
            current_tree.insert_right('right')
            exp_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        else:
            raise ValueError
    return exp_tree


def exp_split(expression):
    """ split support expresions with space and with no space """
    exp = expression.replace(' ', '').lower()
    result = []
    number = ''  # a variable to store number
    boolean = ''  # a variable to store boolean statements
    for i in exp:
        if i not in ['(', ')', '+', '-', '*', '/'] and not i.isalpha():
            number += i
            if boolean != '':
                result.append(boolean)
            boolean = ''  # reset boolean
        elif i.isalpha():
            boolean += i
            if number != '' and is_number(number):
                result.append(float(number))
            number = ''  # reset number
        else:
            # when we meet ['+', '-', '*', '/', 'and', 'or', 'not'], then we add current number to result
            # and set number = ''
            if boolean != '':
                result.append(boolean)
            boolean = ''  # reset boolean
            if number != '' and is_number(number):
                result.append(float(number))
            number = ''  # reset number
            result.append(i)
    return result


def is_number(i):
    """ check if a string is number(int, float, negetive number) """
    try:
        float(i)
        return True
    except ValueError:
        return False


def evaluate(tree: BinaryTree):
    """ evaluate the parse tree """
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul,
                 '/': operator.truediv, 'and': fn_and, 'or': fn_or, 'not': fn_not}
    left = tree.get_left_child()
    right = tree.get_right_child()
    if tree.get_root_val() == 'not':
        fn = operators[tree.get_root_val()]
        return fn(right)
    else:
        if left and right:  # if a node has left and right, so this node must be a operator
            fn = operators[tree.get_root_val()]
            return fn(evaluate(left), evaluate(right))
        else:  # leaf noede
            return (tree.get_root_val())


def fn_and(a, b):
    return a and b


def fn_or(a, b):
    return a or b


def fn_not(a):
    return not a


def print_exp(tree):
    exp = ''
    if tree:
        if type(tree.get_left_child()) == BinaryTree:
            exp = '(' + print_exp(tree.get_left_child())
        else:
            exp = print_exp(tree.get_left_child())
        exp = exp + str(tree.get_root_val())
        if type(tree.get_right_child()) == BinaryTree:
            exp = exp + print_exp(tree.get_right_child()) + ')'
        else:
            exp = exp + print_exp(tree.get_right_child())
    return exp


if __name__ == '__main__':
    exp1 = '( 31 + ( ( 4 * 5.2 ) / 2 ) )'
    exp_tree1 = build_parse_tree(exp1)
    # print(exp_tree1.post_order_traversal())
    print(print_exp(exp_tree1))
    print(evaluate(exp_tree1))
    
    exp2 = '((not 1) and (1 and 2) or (4 and 4) and (not 5))'
    exp_tree2 = build_parse_tree(exp2)
    # print(exp_tree2.post_order_traversal())
    print(evaluate(exp_tree2))
