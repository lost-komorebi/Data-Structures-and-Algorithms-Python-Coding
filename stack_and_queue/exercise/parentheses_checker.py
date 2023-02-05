#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
write an algorithm that will read a string of parentheses from left to right
and decide whether the symbols are balanced
"""


class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        s = self.items.pop()
        return s

    def is_empty(self):
        return self.items == []


def checker(my_str):
    """
    iterate all parentheses, if it's an opening symbol, push into a stack,
    otherwise pop it from the stack
    after iteration, check whether the stack is empty and balanced
    """
    balanced = True  # assume parentheses are balanced
    my_stack = Stack()
    for i in my_str:
        if i == '(':
            my_stack.push(i)
        else:
            if my_stack.is_empty():
                balanced = False
            else:
                my_stack.pop()

    return my_stack.is_empty() and balanced


if __name__ == '__main__':
    parentheses = ['(()()()())',
                   '(((())))',
                   '(()((())()))',
                   '((((((())',
                   '()))',
                   '(()()(()']
    for parenthesis in parentheses:
        print(checker(parenthesis))
