#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
""" this *.py using a no limitation list to perform a stack """


class StackListNoLimit:
    def __init__(self):
        self.list = []

    def __repr__(self):
        return '\n'.join(map(str, reversed(self.list)))

    def push(self, data):
        self.list.append(data)

    def pop(self):
        if self.is_empty():
            raise Exception('pop from empty stack')
        return self.list.pop()

    def peek(self):
        if self.is_empty():
            raise Exception('Empty stack')
        return self.list[-1]

    def is_empty(self):
        if not self.list:  # empty list is False
            return True
        return False

    def delete_stack(self):
        self.list = []


my_stack = StackListNoLimit()
print(my_stack.is_empty())

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack)
my_stack.pop()
print(my_stack.peek())
