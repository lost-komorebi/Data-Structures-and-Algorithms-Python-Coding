#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
""" this *.py using a no limitation list to perform a stack """


class StackListLimit:
    def __init__(self, length):
        self.list = []
        self.length = length

    def __repr__(self):
        return '\n'.join(map(str, reversed(self.list)))

    def push(self, data):
        if self.is_full():
            raise Exception('This stack is full')
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

    def is_full(self):
        if len(self.list) == self.length:
            return True
        return False

    def delete_stack(self):
        self.list = []


my_stack = StackListLimit(10)
print(my_stack.is_empty())
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack)
my_stack.pop()
print(my_stack.peek())
for i in range(1, 10):
    my_stack.push(i)
